import Ember from 'ember';
import Route from '@ember/routing/route';
import { inject as service } from '@ember/service';

export default Ember.Route.extend({
  store: service(),

  beforeModel(transition){
    let blah = this;
    setTimeout(function(){
      if(!blah.get('auth.isLoggedIn')){
        this.transitionTo('login');
      }
    }, 2000);
  },

  setupController(controller, model) {
    this._super(controller, model);
    //this.controller.set('form.profile', '');
    this.controller.set('form.commtype', '');
    this.controller.set('form.description', '');
    this.controller.set('form.price_min', '');
    this.controller.set('form.price_max', '');
    this.controller.set('form.slots', '');
  },

  actions:{
    create() {
      const form = this.controller.get('form');
      const store = this.get('store');
      var profileData = this.get('auth.profile');
      //var profileData = this.store.find('profile', this.get('auth.userid'));
      /*this.store.find('profile', 1).then(function(profile) {
        newCommission.set('profile', profile);
      });*/
      console.log(profileData.get('id'));
      const newCommission = store.createRecord('commission', {
        profile: this.get('auth.profile'),
        commtype: form.commtype,
        description: form.description,
        price_min : form.price_min,
        price_max : form.price_max,
        slots : form.slots,
      });
      let context = this;
      //newCommission.get('id');

      newCommission.save()
        .then(() => {
          context.transitionTo('index');
        });
     },
     cancel() {
       this.transitionTo('index');
     }
  }
});

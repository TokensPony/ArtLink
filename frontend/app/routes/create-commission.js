import Ember from 'ember';
import Route from '@ember/routing/route';
import { inject as service } from '@ember/service';

export default Ember.Route.extend({
  store: service(),
  auth: Ember.inject.service('auth-manager'),

  //Prevents access from users not logged in
  beforeModel(transition){
    let blah = this;
    //setTimeout(1000);
    //console.log(transition);
    if(!blah.get('auth.isLoggedIn')){
      blah.transitionTo('login');
    }
  },

  //Sets up the form for new Commissions defined in the controller
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
    //Creates new commission data on backend and frontend, then goes to index
    create() {
      const form = this.controller.get('form');
      const store = this.get('store');
      var profileData = this.get('auth.profile');
      //console.log(profileData.get('id'));
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

import Ember from 'ember';
import Route from '@ember/routing/route';
import { inject as service } from '@ember/service';

export default Ember.Route.extend({
  store: service(),

  setupController(controller, model) {
    this._super(controller, model);
    this.controller.set('form.profile', '');
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
      var profileData = this.store.find('profile', 1);
      /*this.store.find('profile', 1).then(function(profile) {
        newCommission.set('profile', profile);
      });*/
      const newCommission = store.createRecord('commission', {
        profile: profileData,
        commtype: form.commtype,
        description: form.description,
        price_min : form.price_min,
        price_max : form.price_max,
        slots : form.slots,
      });

      newCommission.get('id');

      newCommission.save()
        .then(() => {
          this.transitionTo('index');
        });
     },
     cancel() {
       this.transitionTo('index');
     }
  }
});

import Ember from 'ember';
import Controller from '@ember/controller';
import { computed } from '@ember/object';

export default Ember.Controller.extend({
    form: computed(function() {
      return{
        commtype: '',
        description: '',
        price_min: '',
        price_max: '',
        slots: ''
      }
    })
});

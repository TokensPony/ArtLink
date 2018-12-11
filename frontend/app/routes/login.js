import Ember from 'ember';

export default Ember.Route.extend({
  beforeModel(transition){
    if(!this.get('auth.isLoggedIn')){
      this.transitionTo('index');
    }
  },
});

import Ember from 'ember';

export default Ember.Route.extend({
  auth: Ember.inject.service('auth-manager'),
  beforeModel(transition){
    let blah = this;
    console.log(blah.get('auth.isLoggedIn'));
    if(blah.get('auth.isLoggedIn')){
        blah.transitionTo('index');
    }
  },
});

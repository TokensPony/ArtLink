import Ember from 'ember';

export default Ember.Route.extend({
  auth: Ember.inject.service('auth-manager'),
  //Prevents access from logged in users
  beforeModel(transition){
    let blah = this;
    console.log(blah.get('auth.isLoggedIn'));
    if(blah.get('auth.isLoggedIn')){
        blah.transitionTo('index');
    }
  },
});

import Ember from 'ember';
import config from './config/environment';

const Router = Ember.Router.extend({
  location: config.locationType,
  rootURL: config.bURL
});

Router.map(function() {
  this.route('login');
  this.route('createaccount');
  //this.route('profile');
  this.route('profile', {
    path: '/:profile'
  }, function() {});
  this.route('commissions');
});

export default Router;

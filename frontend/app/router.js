import Ember from 'ember';
import config from './config/environment';

const Router = Ember.Router.extend({
  location: config.locationType,
  rootURL: config.bURL
});

Router.map(function() {
  this.route('login');
  this.route('createaccount');
});

export default Router;

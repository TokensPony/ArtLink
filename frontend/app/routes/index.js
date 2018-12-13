import Ember from 'ember';


var defaultitems = Ember.A([
  {
    title: 'ArtLink',
    description: 'Exciting stuff!',
    img: 'img/NGC-logo.png',
    link: '',

  },
	{
		title: 'Masonry-based Event Display Template',
		description: 'You are seeing this template, because you haven\'t loaded any data into your client yet. This Template will be used to display events as they load from your REST API.',
    img: 'img/template-icon.svg',
    link: 'index'

	},


]);

export default Ember.Route.extend({
  //router: Ember.inject.service('-router'),

  actions: {
    willTransition(transition){
      let blah = this;
      console.log(transition.targetName);

    }
  },
	model() {
    return this.store.findAll('profile');
    /*return this.store.findAll('profile').then(function(list){
      return list.filterBy("commstatus", "Open");
    });*/
    //return this.store.queryRecord('profile', {filter: {user : 9}})
	},
  setupController(controller, model){
    this._super(controller, model);
    controller.set('defaultitems', defaultitems);
    var route = this;
    /*setInterval(Ember.run.later(route, function() {
      // code here will execute within a RunLoop about every minute
      if(controller.get('auth.isLoggedIn')){
        route.getData().then(function(data){
          if(data[0].id!=controller.get('content')[0].id){
            controller.get('content').insertAt(0, data[0]);
          }
        });
      }
    }, 5), 3000);*/
  }
});

import Ember from 'ember';

export default Ember.Route.extend({
  /*getData(){
    console.log(arguments[0]);
    var items = Ember.A([]);
    return Ember.$.get('/api/profiles/' + arguments[0]).then(function(events){
      events.forEach(function(event){
        // console.log(event);
        var uName = event.user.username;
        var picLink = 'img/no-image.jpg';
        if(uName == "Typhlosion95"){
          picLink = 'img/typhlosion95.jpg';
        }
        items.addObject({
          id: event.user.id,
          username: event.user.username,
		      commstatus: event.commstatus,
		      description: event.description,
          user: event.user,
          img: picLink,
          link_external: '/api/profiles/' + event.user.id
        });
      });
      console.log(items);
      return items.reverse()
    }, function(msg){//error
      console.log('Error loading events:');
      console.log(msg.statusText);
    });
  },*/
	model(params) {
    return this.store.findAll('profile');
	},
  setupController(controller, model){
    controller.set('content', model)
    /*this._super(controller, model);
    controller.set('defaultitems', defaultitems);
    var route = this;
    setInterval(Ember.run.later(route, function() {
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

/**export default Ember.Route.extend({
  getData(){
    //var testVar = params.profile;
    //return testVar;
  },
  model(params) {
    var testVar = params.profile;
    console.log(testVar);
    return testVar;
	}
});*/

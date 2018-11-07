import Ember from 'ember';

export default Ember.Controller.extend({
  showMenu: '',
  actions: {
    toggleMenu(){
      if (this.get('showMenu')){
        this.set('showMenu', '');
      }
      else{
        this.set('showMenu', 'active');
      }

    },
    logout(){
      this.get('auth').logout();
    },
    testPost(){
      var data = {
    		commstatus: 'Open',
    		user: 1,
    		description: 'Hi, I\'m a new artist person and I will work for cheap!'
      };

      Ember.$.ajax({
        url:'/api/profiles/',
        type:"POST",
        data: JSON.stringify(data),
        contentType:"application/json",
        dataType:"json",
        success: function(response){
          console.log('Attempting to turn ifttt on. Response from server is: ');
          console.log(response);
        }
      });
    },
    createNew(){
      var newprofile = this.store.createRecord('profile', {
        commstatus: 'Open',
    		name: 'Tester Name',
    		description: 'Hi, I\'m a new artist person and I will work for cheap!'
      });
      newprofile.save();
    }
  }
});

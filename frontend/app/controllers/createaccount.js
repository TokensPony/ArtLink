import Ember from 'ember';

export default Ember.Controller.extend({
  showMenu: '',
  actions: {
    createAccount(){
      var data = {
        username: this.get('username'),
        password: this.get('password'),
        email: this.get('email'),
        commstatus: 'Open'
      };

      Ember.$.ajax({
        url:'/api/register',
        type:"POST",
        data: JSON.stringify(data),
        contentType:"application/json",
        dataType:"json",
        success: function(response){
          console.log('Attempting to turn ifttt on. Response from server is: ');
          console.log(response);
        }
      });
    }
  }
});

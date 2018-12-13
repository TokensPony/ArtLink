import Ember from 'ember';

export default Ember.Controller.extend({
  auth: Ember.inject.service('auth-manager'),
  showMenu: '',
  actions: {
    /*Creates the account for a new user and passes default information for building
    a corresponding profile with the user.*/
    createAccount(){
      var context = this;
      var data = {
        username: this.get('auth.username'),
        password: this.get('auth.password'),
        email: this.get('auth.email'),
        commstatus: 'Open',
        artstyle: 'Digital',
        willdraw: 'MLP, Undertale',
        wontdraw: 'Family Guy'
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
      //If successful, then it automatically logs in the user
      }).then(function(response){
        //Authenticate
        console.log(response);
        context.set('auth.email', '');
        context.get('auth').login();
      });
      //this.transitionToRoute('index');
    }
  }
});

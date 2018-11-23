// app/serializers/application.js
export default DS.JSONAPISerializer.extend({
    keyForAttribute: function(key) {
        return Ember.String.decamelize(key);
    },

    keyForRelationship: function(key) {
        return Ember.String.decamelize(key);
    }
});

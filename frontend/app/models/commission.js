import DS from 'ember-data';

export default DS.Model.extend({
  user: DS.belongsTo('user'),
  commtype: DS.attr('string'),
  description: DS.attr('string'),
  price_min: DS.attr('number'),
  price_max: DS.attr('number'),
  slots: DS.attr('number')
});

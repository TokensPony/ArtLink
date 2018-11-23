import DS from 'ember-data';

export default DS.Model.extend({
  profile: DS.belongsTo('profile'),
  commtype: DS.attr('string'),
  description: DS.attr('string'),
  price_min: DS.attr('number'),
  price_max: DS.attr('number'),
  slots: DS.attr('number')
});

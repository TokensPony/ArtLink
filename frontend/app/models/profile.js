import DS from 'ember-data';

export default DS.Model.extend({
    user: DS.belongsTo('user'),
    commstatus: DS.attr('string'),
    description: DS.attr('string'),
    artstyle: DS.attr('string'),
    willdraw: DS.attr('string'),
    wontdraw: DS.attr('string'),
});

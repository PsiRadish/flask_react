var React = require('react');
var SearchForm = require('./SearchForm');
var Navigation = require('./Navigation');
var CreateFighter = require('./CreateFighter');

module.exports = React.createClass({
  render: function(){
    return (
        <div>
            <Navigation />
            <SearchForm />
            <CreateFighter />

        </div>
    )
  }
});

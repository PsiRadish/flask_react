var React = require('react');
var FighterResult = require('./FighterResult');

module.exports = React.createClass({

  getDefaultProps: function(){
    return {results:[]};
  },

  render: function(){
    var fighterResult = this.props.fighters.map(function(fighter,idx){
      return (
        <div class="well">
          <FighterResult fighter={fighter} key={idx} />

        </div>
        )
    });

    return (
      <div>
            {fighterResult}
      </div>
    )
  }
})
var React = require('react');
var FighterResult = require('./FighterResult');

module.exports = React.createClass({

  getDefaultProps: function(){
    return {results:[]};
  },

  render: function(){
    var fighterResult = this.props.fighters.map(function(fighter,idx){
      return (
        <div class="col-xs-3 col-sm-3 col-md-3 col-lg-3">
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
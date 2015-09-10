var React = require('React');

var React = require('react');

module.exports = React.createClass({
  render: function() {
    var item = this.props.fighter;
    var moveList = item.moves.map(function(move,idx){
        return (
                <li key={idx}>{move.name}</li>
            )
    });
    return (
      <div class="thumbnail">

            <div className="col-xs-6 col-sm-6 col-md-6 col-lg-6">
                <h2><a href={'/api/fighter/'+ item.id}>{item.name}</a></h2>
                <h3>{item.blood_type}</h3>
                <h3>{item.gender}</h3>
                <div className="thumb"><img src={item.img_src} /></div>
            </div>
            <div className="col-xs-6 col-sm-6 col-md-6 col-lg-6">
                <ul>
                    {moveList}
                </ul>
            </div>
    </div>

    );
  }
})

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
            <div class="well">

                <tr>
                    <td>
                        <h2><a href={'/api/fighter/'+ item.id}>{item.name}</a></h2>
                        <div className="thumb">
                            <img src={item.img_src} />
                        </div>
                    </td>
                        <td>
                        <h5>blood type:</h5>
                        <h4>{item.blood_type}</h4>
                    </td>
                    <td>
                        <h5>gender:</h5>
                        <h4>{item.gender}</h4>
                        <div className="overflow-list-box">
                            <ul>
                                {moveList}
                            </ul>
                        </div>
                    </td>
                </tr>
            </div>


    );
  }
})

var React = require('react');

module.exports = React.createClass({
    propTypes: {
        onUpdate: React.PropTypes.func.isRequired
    },
    create: function(e){
        e.preventDefault();
        var firstName = this.refs.firstName.getDOMNode().value;
        var lastName = this.refs.lastName.getDOMNode().value;
        var moves = this.refs.moves.getDOMNode().value;
        var description = this.refs.description.getDOMNode().value;
        var imgUrl = this.refs.imgUrl.getDOMNode().value;
        var fighter = {
            firstName:firstName,
            lastName:lastName,
            moves:moves,
            description:description,
            imgUrl:imgUrl
        };
        this.props.onUpdate(fighter)
        return console.log(fighter)
    },
    render: function(){
        return (
            <form onSubmit={this.create} className="form">
                <legend>Form title</legend>

                <div className="form-group">
                    <input type="text" className="form-control" ref="firstName" placeholder="Type a First Name" />
                    <input type="text" className="form-control" ref="lastName" placeholder="Type a Last Name" />
                    <input type="text" className="form-control" ref="moves" placeholder="Type some moves" />
                    <textarea className="form-control" ref="description" placeholder="Type some description" />
                    <input type="text" className="form-control" ref="imgUrl" placeholder="Add an image url of your fighter" />
                </div>
                <button type="submit" className="btn btn-primary">Submit</button>
            </form>
        )
    }
});

// post to api/fighter




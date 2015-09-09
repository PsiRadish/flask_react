var React = require('react');

module.exports = React.createClass({
    // propTypes: {
    //     onUpdate: React.PropTypes.func.isRequired
    // },
    render: function() {
        return (
            <div id="fighterSearch" className="row">
                <div className="col-xs-3 col-sm-3 col-md-3 col-lg-3">

                </div>
                <div className="col-xs-6 col-sm-6 col-md-6 col-lg-6">

                <form className="form">
                    <input ref="textInput" type="text" placeholder="Find a fighter" className="form-control" />
                    <input type="submit" value="search" className="btn btn-default" />
                </form>
                </div>
                <div className="col-xs-3 col-sm-3 col-md-3 col-lg-3">

                </div>
            </div>
        )
    }
});
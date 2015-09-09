var React = require('react');
var SearchForm = require('./SearchForm');
var Navigation = require('./Navigation');
var CreateFighter = require('./CreateFighter');

module.exports = React.createClass({
    getInitialState: function(){
        return {newFighter:'',createdFighter:''}
    },
    createFighter: function(fighter){
        this.setState({newFighter:fighter});
        // console.log(this.state.newFighter.lastName);
        var self = this;
        var ajax = new XMLHttpRequest();
        ajax.addEventListener('load',function(){
            try {
                var data = JSON.parse(this.responseText);
                self.setState({createdFighter:data.results});
            } catch(e) {
                self.setState({createdFighter:''});
            }
        });
        ajax.open('POST','our api url' + '/:' + newFighter.firstName + '/:' + newFighter.lastName + '/:' + newFighter.moves + '/:' + newFighter.description + '/:' + newFighter.imgUrl);
        ajax.send();

    },
    render: function(){
        return (
            <div>
                <Navigation />
                <SearchForm />
                <CreateFighter onUpdate={this.createFighter}/>

            </div>
        )
    }
});

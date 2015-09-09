var React = require('react');
var SearchForm = require('./SearchForm');
var Navigation = require('./Navigation');
var CreateFighter = require('./CreateFighter');

module.exports = React.createClass({
    getInitialState: function(){
        return {createdFighter:'',newFighter:'',fighters:[]}
    },
    getAllFighters: function(){
        var self = this;
        console.log('getAllFighters has been called');
        var ajax = new XMLHttpRequest();
        ajax.addEventListener('load',function(){
            try {
                var data = JSON.parse(this.responseText);
                self.setState({fighters:data});
                console.log(this.state.fighters);
            } catch(e) {
                console.log('something went wrong with request')
                self.setState({fighters:[]});
            }
        });
        ajax.open('GET','/api/fighter',true);
        ajax.send();
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
                <button onClick={this.getAllFighters}>get fighters</button>

            </div>
        )
    }
});

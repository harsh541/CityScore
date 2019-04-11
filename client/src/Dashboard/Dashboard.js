import React, { Component } from 'react';
import { withStyles } from '@material-ui/core/styles';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';

import ScoresTable from '../ScoreTable/ScoreTable';
import TotalScoreChart from '../TotalScoreChart/TotalScoreChart';
const styles = {
  root: {
    flexGrow: 1,
  },
};

class Dashboard extends Component {
  componentDidMount() {
    fetch("http://localhost:5000", {method: 'GET', dataType:'json'})
      .then(r => r.json())
      .then(r => {
        console.log(r)
      })
      .catch(err => console.log(err))
  }
  render() {
    return (
      <div style={{backgroundColor: "#FFF"}}>
        <AppBar position="static" color="default">
          <Toolbar>
            <Typography variant="h6" color="inherit">
              CityScore Chelsea
            </Typography>
          </Toolbar>
        </AppBar>
        <Card>
          <CardContent>
            <Typography>
              Today's Score
            </Typography>
            <div style={{textAlign: "center", display: "inline-block"}}>
              <TotalScoreChart/>
            </div>
          </CardContent>
        </Card>
        <ScoresTable/>
      </div>
    )
  }
}

export default withStyles(styles)(Dashboard);
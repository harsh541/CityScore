import React, { Component } from 'react';
import { withStyles } from '@material-ui/core/styles';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import TotalScore from '../TotalScore/TotalScore';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import ScoresTable from '../ScoreTable/ScoreTable';
import Descriptions from '../Descriptions/Descriptions'
const styles = {
  root: {
    flexGrow: 1,
  },
  card: {
    minWidth: 275,
  },
  title: {
    fontSize: 14,
  },
  pos: {
    marginBottom: 12,
  },
};

class Dashboard extends Component {
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
              <TotalScore/>
            </div>
          </CardContent>
        </Card>
        <ScoresTable/>
        <AppBar position="static" color="default">
          <Toolbar>
            <Typography variant="h7" color="inherit">
              How are the scores calculated?
            </Typography>
          </Toolbar>
        </AppBar>
        <Descriptions/>
      </div>
    )
  }
}

export default withStyles(styles)(Dashboard);
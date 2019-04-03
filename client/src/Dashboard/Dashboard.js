import React, { Component } from 'react';
import { withStyles } from '@material-ui/core/styles';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';

import ScoresTable from '../ScoreTable/ScoreTable';

const styles = {
  root: {
    flexGrow: 1,
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
        <ScoresTable/>
      </div>
    )
  }
}

export default withStyles(styles)(Dashboard);
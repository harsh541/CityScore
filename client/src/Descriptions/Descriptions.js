import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { withStyles } from '@material-ui/core/styles';
import ExpansionPanel from '@material-ui/core/ExpansionPanel';
import ExpansionPanelSummary from '@material-ui/core/ExpansionPanelSummary';
import ExpansionPanelDetails from '@material-ui/core/ExpansionPanelDetails';
import Typography from '@material-ui/core/Typography';
import ExpandMoreIcon from '@material-ui/icons/ExpandMore';

const styles = theme => ({
  root: {
    width: '100%',
  },
  heading: {
    fontSize: theme.typography.pxToRem(15),
    fontWeight: theme.typography.fontWeightRegular,
  },
});


function SimpleExpansionPanel(props) {
  const { classes } = props;
  return (
    <div className={classes.root}>
      <ExpansionPanel>
        <ExpansionPanelSummary expandIcon={<ExpandMoreIcon />}>
          <Typography className={classes.heading}>Graffitti Removal On-Time %</Typography>
        </ExpansionPanelSummary>
        <ExpansionPanelDetails>
          <Typography>
            The removal of graffiti on public property as requested by Chelsea residents. We aim to remove this graffiti reported within 7 business days.
          </Typography>
        </ExpansionPanelDetails>
      </ExpansionPanel>
      <ExpansionPanel>
        <ExpansionPanelSummary expandIcon={<ExpandMoreIcon />}>
          <Typography className={classes.heading}>Streetlight Outages On-Time %</Typography>
        </ExpansionPanelSummary>
        <ExpansionPanelDetails>
          <Typography>
            We aim to repair the streetlight outages reported within 7 business days.
          </Typography>
        </ExpansionPanelDetails>
      </ExpansionPanel>
      <ExpansionPanel>
        <ExpansionPanelSummary expandIcon={<ExpandMoreIcon />}>
          <Typography className={classes.heading}>Missed Trash On-Time %</Typography>
        </ExpansionPanelSummary>
        <ExpansionPanelDetails>
          <Typography align = "left">
          If your trash or recyling was put out on time but was not picked up, we will send a crew to inspect. We aim to inspect the missed trash reported within 7 business days.
          </Typography>
        </ExpansionPanelDetails>
      </ExpansionPanel>
      <ExpansionPanel>
        <ExpansionPanelSummary expandIcon={<ExpandMoreIcon />}>
          <Typography className={classes.heading}>Pothole Repair On-Time %</Typography>
        </ExpansionPanelSummary>
        <ExpansionPanelDetails>
          <Typography align = "left">
          We aim to repair potholes to increase safety and reduce vehicular damage. We aim to repair the potholes reported within 7 business days.
          </Typography>
        </ExpansionPanelDetails>
      </ExpansionPanel>
      <ExpansionPanel>
        <ExpansionPanelSummary expandIcon={<ExpandMoreIcon />}>
          <Typography className={classes.heading}>Robbings</Typography>
        </ExpansionPanelSummary>
        <ExpansionPanelDetails>
          <Typography align = "left">
          A CityScore greater than 1 indicates a decrease in robbings relative to the historical average.
          </Typography>
        </ExpansionPanelDetails>
      </ExpansionPanel>
       <ExpansionPanel>
        <ExpansionPanelSummary expandIcon={<ExpandMoreIcon />}>
          <Typography className={classes.heading}>Assaults</Typography>
        </ExpansionPanelSummary>
        <ExpansionPanelDetails>
          <Typography align = "left">
          A CityScore greater than 1 indicates a decrease in assaults relative to the historical average.
          </Typography>
        </ExpansionPanelDetails>
      </ExpansionPanel>
       <ExpansionPanel>
        <ExpansionPanelSummary expandIcon={<ExpandMoreIcon />}>
          <Typography className={classes.heading}>Thefts</Typography>
        </ExpansionPanelSummary>
        <ExpansionPanelDetails>
          <Typography align = "left">
          A CityScore greater than 1 indicates a decrease in thefts relative to the historical average.
          </Typography>
        </ExpansionPanelDetails>
      </ExpansionPanel>
    </div>
  );
}

SimpleExpansionPanel.propTypes = {
  classes: PropTypes.object.isRequired,
};

export default withStyles(styles)(SimpleExpansionPanel);
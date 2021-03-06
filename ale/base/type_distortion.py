class RadialDistortion():
    @property
    def usgscsm_distortion_model(self):
        """
        Expects odtk to be defined. This should be a list containing
        the radial distortion coefficients 

        Returns
        -------
        : dict
          Dictionary containing the usgscsm distortion model
        """
        return {
            "radial": {
                "coefficients" : self.odtk
            }
        }


class NoDistortion():
    @property
    def usgscsm_distortion_model(self):
        """
        Returns the specification for no distortion in usgscsm.
        
        Returns
        -------
        : dict
          Dictionary containing the usgscsm specification for no distortion.
        """
        return {"radial": {"coefficients": [0.0, 0.0, 0.0]}}

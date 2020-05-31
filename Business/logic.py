class Logic(object):
    """
    This class is useful
    """
    combinational = {
        "LUT4_L",
        "LUT5",
        "LUT5_L",
        "LUT6",
        "LUT6_L",
        "INV",
        "LUT3",
        "LUT2",
        "LUT4",
        "MUXF5",
        "MUXF8",
        "MUXF7",
        "LUT3_L",
        "BUFGP",
    }

    sequential = {
        "FDD",
        "FDE",
        "FDC_1",
        "FDC",
        "FDCE",
        "FD",
        "FDPE",
        "FDP",
        "FDRE",
        "FDRSE",
        "FDR",
        "FDS",
        "FDSE",
        "FDRS",
    }

    @classmethod
    def is_combinational(cls, value):
        """I dont know"""
        return value in cls.combinational

    @classmethod
    def is_sequential(cls, value):
        return value in cls.sequential
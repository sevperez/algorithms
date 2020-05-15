class OpCounter:
    """
    - OpCounter object with its self.count initialized to 0.
    - Usage:
      - Initialize an OpCounter object, oc = OpCounter()
      - Insert a call to the oc object in the relevant sections of
        the function you are analyzing. For example, inside any
        loops.
      - After running your function, oc.count will contain the 
        number of times the object was called. For example, if you
        included it in 2 loops that ran n times each, then oc.count
        will equal 2n.
    """

    def __init__(self):
        self.count = 0

    def __call__(self):
        self.count += 1

    def reset(self):
        """
        - Resets self.count to 0.
        """
        self.count = 0

### LOGIC GATES HELPER FUNCTION CLASS ###
class LogicGatesExtension:
    @staticmethod
    def apply_and(self, a, b, out):
        self.ccx(a, b, out)

    @staticmethod
    def apply_or(self, a, b, out):
        self.cx(a, out)
        self.cx(b, out)
        self.ccx(a, b, out)

    @staticmethod
    def apply_xor(self, a, b, out):
        self.cx(a, out)
        self.cx(b, out)

    @staticmethod
    def apply_controlled_and(self, c, a, b, out):
        self.mcx([c, a, b], out)
    
    @staticmethod
    def apply_controlled_or(self, c, a, b, out):
        self.mcx([c, a], out)
        self.mcx([c, b], out)
        self.mcx([c, a, b], out)
    
    @staticmethod
    def apply_controlled_xor(self, c, a, b, out):
        self.mcx([c, a], out)
        self.mcx([c, b], out)
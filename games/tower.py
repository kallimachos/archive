class disc :
    # create a disc, assigning it a name (so we can watch it better)
    # an initial peg, and a reference to the next smaller disc
    # or the value None if this is to be the smallest disc

    def __init__ (self, name, peg, nextSmaller) :
        self.name = name
        self.peg  = peg
        self.nextSmaller = nextSmaller

    # when asked to move to a new peg, find the alternate peg by starting
    # with a list of all 3 and removing the 2 I can't use.
    # then move everything above me to the alternate peg
    # then move myself (change my peg value).
    # Finally move the smaller pegs back on top of me

    def move (self,newPeg) :
#        print self.name,": I have been requested to move to peg", newPeg
        if self.nextSmaller :
            pegs = [1,2,3]           # find what has to be the alternate peg
            pegs.remove(newPeg)      # can't be the one I'm going to
            pegs.remove(self.peg)    # can't be the one we're on
            altPeg = pegs[0]         # Ahh. That one.

#            print self.name,": Asking",self.nextSmaller.name,
#           print "to get out of my way and move to peg",altPeg
            self.nextSmaller.move(altPeg)

#            print self.name, ": Moving to", newPeg
            self.peg = newPeg
            show_grid()

#            print self.name,": Asking",self.nextSmaller.name,
#            print "to rejoin me on peg",self.peg
            self.nextSmaller.move(self.peg)
        else :
            # If I'm the smallest disc, life is very simple
#            print self.name, ": Moving to", newPeg
            self.peg = newPeg
            show_grid()

# Make 3 discs all on peg 1. 'A' is the largest and on the bottom
c = disc("C",1, None)   # the smallest disc. No nextSmaller disc
b = disc("B",1, c)      # 2nd largest disc
a = disc("A",1, b)      # largest disc

def set_disc(grid, peg, name):
	if grid[2][peg-1] == ".":
		grid[2][peg-1] = name
	elif grid[1][peg-1] == ".":
		grid[1][peg-1] = name
	else: grid[0][peg-1] = name

def show_grid():
	grid = []
	for n in range(3):
		grid.append(["."] * 3)
	set_disc(grid, a.peg, a.name)
	set_disc(grid, b.peg, b.name)
	set_disc(grid, c.peg, c.name)
	for row in grid:
		print " ".join(row)
	print ""

def test() :
    show_grid()
    a.move(3)               # Now move all the discs to peg 3

test()

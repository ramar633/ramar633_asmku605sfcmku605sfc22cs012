#define the player class
class player:
  def play(self):
    print("the palyer is playing cricket.")
    #define the batsman class,derived from player
    class batsman(player):
      def play(Self):
        print("the batsman is batting.")
        #define the bowler class,derived from player
        class bowler(player):
          def play(self):
            print("the bowler is bowling.")
            #create objects of batsman and bowler classes
            batsman=Batsman()
            bowler=Bowler()
            #call the play()method for each object
            batsman.play()
            bowler.play()
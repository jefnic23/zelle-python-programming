verses = ['one',
          'two',
          'three',
          'four',
          'five',
          'six',
          'seven',
          'eight',
          'nine',
          'ten'
          ]

activities = ['suck his thumb',
              'tie his shoe',
              'climb a tree',
              'shut the door',
              'take a dive',
              'pick up sticks',
              'pray to heaven',
              'roller skate',
              'check the time',
              'shout "The End"'
              ]

def lyrics(verse, activity):
    print(
        """
        The ants go marching {0} by {0}, hurrah! hurrah!
        The ants go marching {0} by {0}, hurrah! hurrah!
        The ants go marching {0} by {0},
        The little one stops to {1},
        And they all go marching down...
        In the ground...
        To get out...
        Of the rain.
        Boom! Boom! Boom!""".format(verse, activity)
        )

for i, activity in enumerate(activities):
    lyrics(verses[i], activity)

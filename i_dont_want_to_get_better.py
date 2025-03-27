import time
from pygame import mixer

print("screaming, crying, perfect storm.")

print("just dissociate.")

print("the demon rectangle is here babe")

print(
    """ 
              ____----------- _____
\~~~~~~~~~~/~_--~~~------~~~~~     \\
 `---`\  _-~      |                   \\
   _-~  <_         |                     \[]
 / ___     ~~--[""] |      ________-------'_
> /~` \    |-.   `\~~.~~~~~                _ ~ - _
 ~|  ||\%  |       |    ~  ._                ~ _   ~ ._
   `_//|_%  \      |          ~  .              ~-_   /\\
          `--__     |    _-____  /\               ~-_ \/.
               ~--_ /  ,/ -~-_ \ \/          _______---~/
                   ~~-/._<   \ \`~~~~~~~~~~~~~     ##--~/
                         \    ) |`------##---~~~~-~  ) )
                          ~-_/_/                  ~~ ~~
"""
)
mixer.init()
mixer.music.load("./Shoreditch.mp3")
mixer.music.play()
while mixer.music.get_busy():  # wait for music to finish playing
    time.sleep(1)

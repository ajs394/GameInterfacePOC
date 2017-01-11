class MagicMissile(object):
    name = 'Magic Missile'
    spellRange = 5
    maxLevel = 9

    @staticmethod
    def cast(player, level):
        for i in range(level):
            player.messages += ['did ' + str(i + 1) + ' damage']

class FireBall(object):
    name = 'Fire Ball'
    spellRange = 4
    maxLevel = 9

    @staticmethod
    def cast(player, level):
        player.messages += ['did ' + str(5*(level)) + ' damage in a 3x3 grid']

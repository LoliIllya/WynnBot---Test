import discord

# TODO: move here as much data as possible

colors = {
    'DEFAULT': 0x000000,
    'WHITE': 0xFFFFFF,
    'AQUA': 0x1ABC9C,
    'GREEN': 0x2ECC71,
    'BLUE': 0x3498DB,
    'PURPLE': 0x9B59B6,
    'LUMINOUS_VIVID_PINK': 0xE91E63,
    'GOLD': 0xF1C40F,
    'ORANGE': 0xE67E22,
    'RED': 0xE74C3C,
    'GREY': 0x95A5A6,
    'NAVY': 0x34495E,
    'DARK_AQUA': 0x11806A,
    'DARK_GREEN': 0x1F8B4C,
    'DARK_BLUE': 0x206694,
    'DARK_PURPLE': 0x71368A,
    'DARK_VIVID_PINK': 0xAD1457,
    'DARK_GOLD': 0xC27C0E,
    'DARK_ORANGE': 0xA84300,
    'DARK_RED': 0x992D22,
    'DARK_GREY': 0x979C9F,
    'DARKER_GREY': 0x7F8C8D,
    'LIGHT_GREY': 0xBCC0C0,
    'DARK_NAVY': 0x2C3E50,
    'BLURPLE': 0x7289DA,
    'GREYPLE': 0x99AAB5,
    'DARK_BUT_NOT_BLACK': 0x2C2F33,
    'NOT_QUITE_BLACK': 0x23272A
}

embed_colors = {
    'info': 0xFF,  # blue
    'error': 0,  # black
    'moderation': 0xFFFF00,  # yellow
    'normal': 0xFF00  # green
}


# TODO: maybe improve it?
def error_embed(reason: str = 'No reason provided', *, description: str = ''):
    """
    Returns embed for errors
    :param reason: Why did the error happened
    :param description: description of the embed
    :return: discord.Embed
    """
    embed = discord.Embed(title='Error!', description=description)
    embed.add_field(name='Reason:', value=reason)

    return embed


help_embed = {
    'Moderation': {
        'ban': {'syntax': '!ban <user> [reason]', 'info': 'bans the user'},
        'kick': {'syntax': '!mute <user> [reason]', 'info': 'kicks the user'},
        'mute': {'syntax': '!mute <user> [reason]', 'info': 'mutes the user'},
    },
    'Wynncraft': {
        'player': {'syntax': '!profile <player name>', 'info': 'provides info on requested player'},
        'guild': {'syntax': '!guild <guild name>', 'info': 'provides info on requested guild'},
        'territory': {'syntax': '!territory <territory name>', 'info': 'provides info on requested territory'},
        'item': {'syntax': '!item <item name>', 'info': 'provides info on requested item'},
        '-- __note__': {'syntax': 'put more word names between double quotes `\"`', 'info': ''}
    },
    'Info': {
        'poll': {'syntax': '!poll <create|end> <name|message id> [options]', 'info': 'creates/ends poll'},
        'help': {'syntax': '!help', 'info': 'displays this message'}
    }
}

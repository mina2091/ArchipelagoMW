from dataclasses import dataclass

from Options import Choice, Range, Toggle, DeathLink, DefaultOnToggle, OptionGroup, PerGameCommonOptions

"""
Easy:			1
Medium:			2
Hard:			3
Harder:			4
Insane:			5
Easy Demon:		6
Medium Demon:	7
Hard Demon:		8
Insane Demon:	9
Extreme Demon:	10
"""

class ChecksPerLevel(Range):
	"""
	Set the amount of checks per level.
	Each check represents a percentage of completion in a level (5%, 10%, ..., 100%)
	
	Example: "5 checks per level" means you will get checks at 20%, 40%, 60%, 80%, and 100% completion.
	"""
	display_name = "Checks Per Level"
	range_start = 1
	range_end = 20
	default = 5

class OnlyOneDifficulty(Choice):
	"""
	Choose whether all levels should have the same fixed difficulty.

	If false, you can set a custon difficulty range for levels to be chosen from.
	"""
	display_name = "Fixed Difficulty Range"
	option_true = True
	option_false = False
	default = False

class FixedDifficulty(Choice):
	"""
	!!Only used if only_one_difficulty is enabled!!

	Select the fixed difficulty level for all levels.
	"""
	display_name = "Fixed Difficulty Level"
	option_easy = 1
	option_medium = 2
	option_hard = 3
	option_harder = 4
	option_insane = 5
	option_easy_demon = 6
	option_medium_demon = 7
	option_hard_demon = 8
	option_insane_demon = 9
	option_extreme_demon = 10
	default = 6

class MinDiff(Choice):
	"""
	A choice option to set the minimum difficulty level for the game.
	"""
	display_name = "Minimum Difficulty"
	option_easy = 1
	option_medium = 2
	option_hard = 3
	option_harder = 4
	option_insane = 5
	option_easy_demon = 6
	option_medium_demon = 7
	option_hard_demon = 8
	option_insane_demon = 9
	option_extreme_demon = 10
	default = 5

class MaxDiff(Choice):
	"""
	A choice option to set the maximum difficulty level for the game.
	"""
	display_name = "Maximum Difficulty"
	option_easy = 1
	option_medium = 2
	option_hard = 3
	option_harder = 4
	option_insane = 5
	option_easy_demon = 6
	option_medium_demon = 7
	option_hard_demon = 8
	option_insane_demon = 9
	option_extreme_demon = 10
	default = 7

class StartingLevelAmount(Range):
	"""
	Set the amount of levels that you will start with.
	"""
	display_name = "Starting Level Amount"
	range_start = 0
	range_end = 100
	default = 0

class LevelAmount(Range):
	"""
	Set the maximum amount of levels that you can unlock.
	"""
	display_name = "Level Amount"
	range_start = 1
	range_end = 100
	default = 20

class GoalAmount(Range):
	"""
	Set the amount of levels that you will need to finish completely.

	This value has to be smaller than or equal to the Level Amount.
	"""
	display_name = "Goal Amount"
	range_start = 1
	range_end = 100
	default = 5

@dataclass
class GDOptions(PerGameCommonOptions):
	checks_per_level: ChecksPerLevel
	only_one_difficulty: OnlyOneDifficulty
	fixed_difficulty: FixedDifficulty
	min_diff: MinDiff
	max_diff: MaxDiff
	starting_level_amount: StartingLevelAmount
	level_amount: LevelAmount
	goal_amount: GoalAmount
	
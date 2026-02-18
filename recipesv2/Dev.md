What if config order matter? PackageRecipe cannot represent that
misc will be the special case of topicRecipe that contain PackageRecipe, Package under that topic do not know their relationship yet.

Unit: if only contain required field, omit field name and one line it.
PackageRecipe: if <=3 entities(count each list entities), omit field name and one line it
TopicRecipe: if there only 1 PackageRecipe with required field only, one line it


relationship in topic recipes
group by topic in PackageRecipe.supporters

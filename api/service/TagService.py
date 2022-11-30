from models.tags import Tags
from models.post_tags import PostTags
from utils import log

##
# @brief From fieldid and postid TO tags
# TODO: FROM PostTags TO Tags without considering fieldid 
# TODO: (JOIN Seems to Accept only one condition)
#
# @param field_id
# @param post_id
#
# @return Tags ENTITY List
def getPostTags(field_id, post_id):
    results = Tags.query.\
            join(PostTags, (PostTags.tagid==Tags.id)).\
            filter(PostTags.fieldid==field_id, PostTags.postid==post_id)
    return results


    

from multiprocessing import synchronize
from fastapi import Body, status, HTTPException, Depends, APIRouter
from .. import models, schemas, oauth2
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List, Optional

router = APIRouter(prefix="/vote", tags=["Votes"])


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
)
def create_vote(
    vote: schemas.Vote,
    db: Session = Depends(get_db),
    current_user=Depends(oauth2.get_current_user),
):

    post = db.query(models.Post).filter(models.Post.id == vote.post_id).first()

    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id {vote.post_id} does not exist",
        )

    new_vote = models.Vote(post_id=vote.post_id, user_id=current_user.id)

    query = db.query(models.Vote).filter(
        models.Vote.post_id == vote.post_id, models.Vote.user_id == current_user.id
    )

    existing_vote = query.first()

    if vote.vote_dir == 1:

        if existing_vote:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"User {current_user.id} has already voted on post {vote.post_id}",
            )
        db.add(new_vote)
        db.commit()
        numOfVotes = (
            db.query(models.Vote).filter(models.Vote.post_id == vote.post_id).count()
        )
        return {
            "message": f"Successfully added - post {vote.post_id} now has {numOfVotes} votes"
        }

    else:
        if not existing_vote:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Vote for post {vote.post_id} does not exist",
            )
        db.delete(existing_vote, synchronize_session=False)
        db.commit()
        numOfVotes = (
            db.query(models.Vote).filter(models.Vote.post_id == vote.post_id).count()
        )
        return {
            "message": f"Successfully deleted - post {vote.post_id} now has {numOfVotes} votes"
        }

from sqlalchemy import select, update, delete, text, and_
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import Ticket, TicketDetails


async def create_ticket(
        db_session: AsyncSession,
        show_name: str,
        user: str = None,
        price: float = None
) -> int:
    ticket = Ticket(
        show=show_name,
        user=user,
        price=price
    )
    async with db_session.begin():
        db_session.add(ticket)
        await db_session.flush()
        ticket_id = ticket.id
    return ticket_id


async def get_ticket(
        db_session: AsyncSession,
        ticket_id: int
) -> Ticket | None:
    query = select(Ticket).where(Ticket.id == ticket_id)
    async with db_session as session:
        tickets = await session.execute(query)
        return tickets.scalars().first()


async def get_all_tickets_for_show(
        db_session: AsyncSession,
        show_name: str
) -> list[Ticket]:
    async with db_session as session:
        result = await session.execute(
            select(Ticket).filter(Ticket.show == show_name)
        )
        tickets = result.scalars().all()
        return tickets


async def update_ticket_price(
        db_session: AsyncSession,
        ticket_id: int,
        new_price: float
) -> bool:
    query = update(Ticket).where(
        Ticket.id == ticket_id).values(price=new_price)
    async with db_session as session:
        ticket_updated = await session.execute(query)
        if ticket_updated.rowcount == 0:
            return False
        return True


async def update_ticket(
        db_session: AsyncSession,
        ticket_id: int,
        update_ticket_dict: dict
) -> bool:
    query = update(Ticket).where(Ticket.id == ticket_id)
    updating_ticket_values = update_ticket_dict.copy()

    if updating_ticket_values == {}:
        return False

    query = query.values(**updating_ticket_values)

    async with db_session as session:
        result = await session.execute(query)
        await session.commit()
        if result.rowcount == 0:
            return False
    return True


async def update_ticket_details(
        db_session: AsyncSession,
        ticket_id: int,
        updating_ticket_details: dict
) -> bool:
    ticket_query = update(TicketDetails).where(
        TicketDetails.ticket_id == ticket_id
    )
    if updating_ticket_details != {}:
        return False
    ticket_query = ticket_query.values(**updating_ticket_details)
    async with db_session as session:
        result = await session.execute(ticket_query)
        await session.commit()
        if result.rowcount == 0:
            return False
    return True


async def delete_ticket(
        db_session: AsyncSession,
        ticket_id: int
) -> bool:
    async with db_session as session:
        tickets_removed = await session.execute(
            delete(Ticket).where(Ticket.id == ticket_id)
        )
        await session.commit()
        if tickets_removed.rowcount == 0:
            return False
        return True

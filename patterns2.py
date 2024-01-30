from aiogram import Router,types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.filters import Command, StateFilter
import random
router = Router()
def randomprimer1():
    a = str(random.randint(0,101))
    b = str(random.randint(0,101))
    c = str(random.randint(0,101))
    return f'{a}+{b}+{c}'
def randomprimer2():
    a = str(random.randint(0,101))
    b = str(random.randint(0,101))
    return f'{a}*{b}'
def randomprimer3():
    a = str(random.randint(0,101))
    b = str(random.randint(-100,101))
    return f'{a}*{b}'

class Primer(StatesGroup):
    waitfrop1 = State()
    waitfrop2 = State()
    waitfrop3 = State()
    endoftest = State()
  


@router.message(Command("start"))
async def Startmes(message: types.Message):
    await message.answer("Здравствуй, это программа для устного счета, Впиши /starttest чтобы получить 3 вопроса")
@router.message(StateFilter(None), Command('starttest'))
async def prm1(message, state: FSMContext):
    n = randomprimer1()
    await state.update_data(ans1 = eval(n))
    await message.answer(f"Первый пример:{n}") 
    await state.set_state(Primer.waitfrop1)
@router.message(Primer.waitfrop1)
async def Chosen1(message: types.Message, state: FSMContext):
    await state.update_data(prim1 = message)
    m = randomprimer2()
    await message.answer(f"Второй пример:{m}")
    await state.update_data(ans2 = eval(m))
    await state.set_state(Primer.waitfrop2)
@router.message(Primer.waitfrop2)
async def Chosen2(message: types.Message, state: FSMContext):
    await state.update_data(prim2 = message)
    s = randomprimer3()
    await message.answer(f"третий пример:{s}")
    await state.update_data(ans3 = eval(s))
    await state.set_state(Primer.waitfrop3)
@router.message(Primer.waitfrop3)
async def getresult(message: types.Message, state: FSMContext):
    await state.update_data(prim3 = message)
    await message.answer("ВЫ закончили тест, введите /result , чтобы узнать свой результат")
    await state.set_state(Primer.endoftest)
@router.message(Primer.endoftest,Command("result"))
async def getresult(message:types.Message, state: FSMContext):
    user_data = await state.get_data()
    trueprimer = 0
    allprimer = 0
    if str(user_data['prim1']) == str(user_data['ans1']):
        trueprimer+=1
    allprimer +=1
    if str(user_data['prim2']) == str(user_data['ans2']):
        trueprimer +=1
    allprimer+=1
    if str(user_data['prim3']) == str(user_data['ans3']):
        trueprimer +=1
    allprimer+=1
    await message.answer(text = f"Ваши правильные ответы:{trueprimer}, Все ответы:{allprimer} \n ваш ответ 1:{user_data['prim1']}, правильный ответ 1:{user_data['ans1']}")

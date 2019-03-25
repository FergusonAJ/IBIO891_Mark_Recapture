from constants import *
if DO_VISUALS:
    import pygame
import time
from subject import Subject
from trap import Trap

if DO_VISUALS:
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
with open('./output/res.csv', 'w+') as resFP:
    resFP.write('run,M,C,R\n')
    
    for r in range(NUM_ROUNDS):
        
        subjectList = []
        Subject.id = 0

        for i in range(NUM_SUBJECTS):
            subjectList.append(Subject(SCREEN_WIDTH, SCREEN_HEIGHT, MIN_RADIUS, MAX_RADIUS))

        trap1 = Trap(SCREEN_WIDTH, SCREEN_HEIGHT, TRAP_RADIUS)
        trap2 = Trap(SCREEN_WIDTH, SCREEN_HEIGHT, TRAP_RADIUS)
        while(trap1.checkCollision(trap2)):
            trap2 = Trap(SCREEN_WIDTH, SCREEN_HEIGHT, TRAP_RADIUS)
        trap1Set = set()
        trap2Set = set()
        trap1TimeMap = {}
        trap2TimeMap = {}

        prevTime = time.time()
        startTime = time.time()
        done = False
        while not done:
            curTime = time.time()
            deltaTime = curTime - prevTime
            prevTime = curTime 
            if curTime - startTime > TRAP_TIME * 3:
                done = True
                    
            
            #Input
            if DO_VISUALS:
                evt = pygame.event.poll()
                if evt.type == pygame.QUIT:
                    done = True
                if evt.type == pygame.KEYDOWN:
                    if evt.key == pygame.K_q or evt.key == pygame.K_ESCAPE:
                        done = True

            # Update positions
            for sub in subjectList:
                sub.move(deltaTime)
         
            #Update traps
            if(curTime - startTime < TRAP_TIME):
                for sub in subjectList:
                    if trap1.checkCollision(sub):
                        trap1Set.add(sub)
                        if sub.id not in trap1TimeMap.keys():
                            trap1TimeMap[sub.id] = curTime - startTime
            elif(curTime - startTime > TRAP_TIME * 2 and curTime - startTime < TRAP_TIME * 3): 
                for sub in subjectList:
                    if trap2.checkCollision(sub):
                        trap2Set.add(sub)
                        if sub.id not in trap2TimeMap.keys():
                            trap2TimeMap[sub.id] = curTime - startTime
                    
            # Render
            if DO_VISUALS:
                screen.fill((0,0,0))
                if(curTime - startTime < TRAP_TIME):
                    trap1.render(screen)
                elif(curTime - startTime > TRAP_TIME * 2 and curTime - startTime < TRAP_TIME * 3): 
                    trap2.render(screen)
                for sub in subjectList:
                    sub.render(screen)
                pygame.display.flip()

        M = len(trap1Set)
        C = len(trap2Set)

        print('Round', r, 'stats!')
        print('Trap 1 count:', M)
        if VERBOSE:
            for x in trap1Set:
                print('\t', x.id)
        print('Trap 2 count:', C)
        if VERBOSE:
            for x in trap2Set:
                print('\t', x.id)
        R = 0
        for x in trap1Set:
            if x in trap2Set:
                R += 1
        print('Recaptured count:', R)
        if R != 0:
            print('Estimate:', (M * C) / float(R))
        else:
            print('Can\'t estimate! R = 0 causes division by zero!')


        with open('./output/trap_1_' + str(r) + '.csv', 'w+') as fp:
            fp.write('id, radius, time\n')
            for x in trap1Set:
                fp.write(str(x.id) + ', ' + str(x.r) + ',' + str(trap1TimeMap[x.id]) + '\n')

        with open('./output/trap_2_' + str(r) + '.csv', 'w+') as fp:
            fp.write('id, radius, time\n')
            for x in trap2Set:
                fp.write(str(x.id) + ', ' + str(x.r) + ',' + str(trap2TimeMap[x.id]) + '\n')

        resFP.write(str(r))
        resFP.write(',')
        resFP.write(str(M))
        resFP.write(',')
        resFP.write(str(C))
        resFP.write(',')
        resFP.write(str(R))
        resFP.write('\n')

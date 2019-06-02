# -*- encoding=utf8 -*-
__author__ = "Adrian"

from airtest.core.api import *
import sys

auto_setup(__file__)

start_app("dk.tactile.lilysgarden")


wait(Template(r"tpl1559334042755.png", record_pos=(0.18, 0.173), resolution=(2960, 1440)))

touch(Template(r"tpl1559334049238.png", record_pos=(-0.004, 0.181), resolution=(2960, 1440)))
if exists(Template(r"tpl1559334062191.png", record_pos=(-0.003, -0.143), resolution=(2960, 1440))):
    touch(Template(r"tpl1559334069864.png", record_pos=(0.183, -0.142), resolution=(2960, 1440)))

touch(Template(r"tpl1559404415364.png", record_pos=(0.385, 0.17), resolution=(2960, 1440)))
touch(Template(r"tpl1559334094579.png", record_pos=(0.002, 0.127), resolution=(2960, 1440)))
sleep(2)
assert_exists(Template(r"tpl1559401667309.png", record_pos=(-0.444, 0.113), resolution=(2960, 1440)), "Stage start works.")
touch(Template(r"tpl1559401678461.png", record_pos=(-0.305, -0.176), resolution=(2960, 1440)))
while not exists(Template(r"tpl1559338410199.png", record_pos=(-0.003, -0.151), resolution=(2960, 1440))):
    sleep(2)
    if exists(Template(r"tpl1559477408680.png", record_pos=(-0.236, 0.13), resolution=(2960, 1440))):
        assert_exists(Template(r"tpl1559477408680.png", record_pos=(-0.236, 0.13), resolution=(2960, 1440)), "Combo of 2+ horizontal blue flowers exist.")

        touch(Template(r"tpl1559477408680.png", record_pos=(-0.236, 0.13), resolution=(2960, 1440)))
        sleep(2)
        if exists(Template(r"tpl1559338410199.png", record_pos=(-0.003, -0.151), resolution=(2960, 1440))):
            break;
    if exists(Template(r"tpl1559474915894.png", record_pos=(0.17, 0.05), resolution=(2960, 1440))):
        assert_exists(Template(r"tpl1559474915894.png", record_pos=(0.17, 0.05), resolution=(2960, 1440)),"Combo of 2+ blue flowers exist.")

        touch(Template(r"tpl1559474915894.png", record_pos=(0.17, 0.05), resolution=(2960, 1440)))        
        sleep(2)
        if exists(Template(r"tpl1559338410199.png", record_pos=(-0.003, -0.151), resolution=(2960, 1440))):
            break;

    if exists(Template(r"tpl1559398998287.png", record_pos=(0.121, -0.011), resolution=(2960, 1440))):
        assert_exists(Template(r"tpl1559398998287.png", record_pos=(0.121, -0.011), resolution=(2960, 1440)), "Combo of 2+ pink flowers exist.")
        touch(Template(r"tpl1559398998287.png", record_pos=(0.121, -0.011), resolution=(2960, 1440)))
        sleep(2)
        if exists(Template(r"tpl1559338410199.png", record_pos=(-0.003, -0.151), resolution=(2960, 1440))):
            break;

    if exists(Template(r"tpl1559474853737.png", record_pos=(-0.107, 0.142), resolution=(2960, 1440))):
        assert_exists(Template(r"tpl1559474853737.png", record_pos=(-0.107, 0.142), resolution=(2960, 1440)), "Combo of 2+ pink flowers exist.")

        touch(Template(r"tpl1559474853737.png", record_pos=(-0.107, 0.142), resolution=(2960, 1440)))
        sleep(2)
        if exists(Template(r"tpl1559338410199.png", record_pos=(-0.003, -0.151), resolution=(2960, 1440))):
            break;

    if exists(Template(r"tpl1559474806430.png", record_pos=(-0.154, 0.141), resolution=(2960, 1440))):
        assert_exists(Template(r"tpl1559474806430.png", record_pos=(-0.154, 0.141), resolution=(2960, 1440)), "Combo of 2+ yellow flowers exist.")

        touch(Template(r"tpl1559474806430.png", record_pos=(-0.154, 0.141), resolution=(2960, 1440)))
        sleep(2)
        if exists(Template(r"tpl1559338410199.png", record_pos=(-0.003, -0.151), resolution=(2960, 1440))):
            break;

    if exists(Template(r"tpl1559474747098.png", record_pos=(-0.143, -0.055), resolution=(2960, 1440))):
        assert_exists(Template(r"tpl1559474747098.png", record_pos=(-0.143, -0.055), resolution=(2960, 1440)), "Combo of 2+ yellow flowers exist.")
        touch(Template(r"tpl1559474747098.png", record_pos=(-0.143, -0.055), resolution=(2960, 1440)))
        sleep(2)
        if exists(Template(r"tpl1559338410199.png", record_pos=(-0.003, -0.151), resolution=(2960, 1440))):
            break;

    if exists(Template(r"tpl1559338187475.png", record_pos=(-0.107, -0.128), resolution=(2960, 1440))):
        assert_exists(Template(r"tpl1559338192387.png", record_pos=(-0.107, -0.125), resolution=(2960, 1440)),"Combo of 2+ red flowers exist.")
        touch(Template(r"tpl1559338192387.png", record_pos=(-0.107, -0.125), resolution=(2960, 1440)))
        sleep(2)
        if exists(Template(r"tpl1559338410199.png", record_pos=(-0.003, -0.151), resolution=(2960, 1440))):
            break;

    if exists(Template(r"tpl1559338208541.png", record_pos=(0.147, 0.174), resolution=(2960, 1440))):
        assert_exists(Template(r"tpl1559338216266.png", record_pos=(0.145, 0.175), resolution=(2960, 1440)),"Combo of 2+ red flowers exist.")
        touch(Template(r"tpl1559338216266.png", record_pos=(0.145, 0.175), resolution=(2960, 1440)))
        sleep(2)
        if exists(Template(r"tpl1559338410199.png", record_pos=(-0.003, -0.151), resolution=(2960, 1440))):
            break;

    if exists(Template(r"tpl1559474668490.png", record_pos=(0.177, -0.01), resolution=(2960, 1440))):
        assert_exists(Template(r"tpl1559474668490.png", record_pos=(0.177, -0.01), resolution=(2960, 1440)), "Combo of 2+ purple flowers exist.")
        touch(Template(r"tpl1559474668490.png", record_pos=(0.177, -0.01), resolution=(2960, 1440)))

        sleep(2)
        if exists(Template(r"tpl1559338410199.png", record_pos=(-0.003, -0.151), resolution=(2960, 1440))):
            break;

    if exists(Template(r"tpl1559474631273.png", record_pos=(0.216, -0.046), resolution=(2960, 1440))):
        assert_exists(Template(r"tpl1559474631273.png", record_pos=(0.216, -0.046), resolution=(2960, 1440)), "Combo of 2+ purple flowers exist.")
        touch(Template(r"tpl1559474631273.png", record_pos=(0.216, -0.046), resolution=(2960, 1440)))
        sleep(2)
        if exists(Template(r"tpl1559338410199.png", record_pos=(-0.003, -0.151), resolution=(2960, 1440))):
            break;

    if exists(Template(r"tpl1559481667803.png", record_pos=(0.017, 0.108), resolution=(2960, 1440))):
        assert_exists(Template(r"tpl1559481667803.png", record_pos=(0.017, 0.108), resolution=(2960, 1440)),"Combo of 2+ orange flowers exist.")
        touch(Template(r"tpl1559481667803.png", record_pos=(0.017, 0.108), resolution=(2960, 1440)))
        sleep(2) 
        if exists(Template(r"tpl1559338410199.png", record_pos=(-0.003, -0.151), resolution=(2960, 1440))):
            break;
    if exists(Template(r"tpl1559482249765.png", record_pos=(0.285, 0.097), resolution=(2960, 1440))):
        assert_exists(Template(r"tpl1559482249765.png", record_pos=(0.285, 0.097), resolution=(2960, 1440)),"Combo of 2+ orange flowers exist")
        touch(Template(r"tpl1559482249765.png", record_pos=(0.285, 0.097), resolution=(2960, 1440)))
        sleep(2)
        if exists(Template(r"tpl1559338410199.png", record_pos=(-0.003, -0.151), resolution=(2960, 1440))):
            break;


    if exists(Template(r"tpl1559338232407.png", record_pos=(0.215, 0.13), resolution=(2960, 1440))):
        assert_exists(Template(r"tpl1559399389121.png", record_pos=(-0.083, 0.179), resolution=(2960, 1440)), "Diagonal rocket exists.")
        touch(Template(r"tpl1559338240454.png", record_pos=(0.215, 0.131), resolution=(2960, 1440)))
        sleep(2)
        if exists(Template(r"tpl1559338410199.png", record_pos=(-0.003, -0.151), resolution=(2960, 1440))):
            break;

    if exists(Template(r"tpl1559338270352.png", record_pos=(-0.155, -0.054), resolution=(2960, 1440))):
        assert_exists(Template(r"tpl1559399409218.png", record_pos=(0.147, 0.086), resolution=(2960, 1440)), "Horizontal rocket exists.")
        touch(Template(r"tpl1559338277956.png", record_pos=(-0.153, -0.052), resolution=(2960, 1440)))
        sleep(2)
        if exists(Template(r"tpl1559338410199.png", record_pos=(-0.003, -0.151), resolution=(2960, 1440))):
            break;

    if exists(Template(r"tpl1559338304862.png", record_pos=(0.168, 0.086), resolution=(2960, 1440))):
        assert_exists(Template(r"tpl1559399553945.png", record_pos=(-0.176, 0.133), resolution=(2960, 1440)), "Bomb exists.")
        touch(Template(r"tpl1559338311793.png", record_pos=(0.169, 0.086), resolution=(2960, 1440)))
        sleep(2)
        if exists(Template(r"tpl1559338410199.png", record_pos=(-0.003, -0.151), resolution=(2960, 1440))):
            break;

    if exists(Template(r"tpl1559339044617.png", record_pos=(-0.2, 0.038), resolution=(2960, 1440))):
        assert_exists(Template(r"tpl1559399451189.png", record_pos=(-0.176, 0.128), resolution=(2960, 1440)), "Blue rocket combo exists.")
        touch(Template(r"tpl1559339052726.png", record_pos=(-0.2, 0.036), resolution=(2960, 1440)))
        sleep(2)
        if exists(Template(r"tpl1559338410199.png", record_pos=(-0.003, -0.151), resolution=(2960, 1440))):
            break;

    if exists(Template(r"tpl1559339065064.png", record_pos=(-0.155, -0.009), resolution=(2960, 1440))):
        assert_exists(Template(r"tpl1559399590785.png", record_pos=(-0.131, 0.081), resolution=(2960, 1440)), "Yellow rocket combo exists.")
        touch(Template(r"tpl1559339073418.png", record_pos=(-0.154, -0.01), resolution=(2960, 1440)))
        sleep(2)
        if exists(Template(r"tpl1559338410199.png", record_pos=(-0.003, -0.151), resolution=(2960, 1440))):
            break;

    if exists(Template(r"tpl1559339082959.png", record_pos=(0.078, 0.036), resolution=(2960, 1440))):
        assert_exists(Template(r"tpl1559399335898.png", record_pos=(0.147, -0.01), resolution=(2960, 1440)), "Pink rocket combo exists.")
        touch(Template(r"tpl1559339091910.png", record_pos=(0.078, 0.035), resolution=(2960, 1440)))
        sleep(2)
        if exists(Template(r"tpl1559338410199.png", record_pos=(-0.003, -0.151), resolution=(2960, 1440))):
            break;

    if exists(Template(r"tpl1559339105526.png", record_pos=(0.078, 0.127), resolution=(2960, 1440))):
        assert_exists(Template(r"tpl1559339113894.png", record_pos=(0.077, 0.128), resolution=(2960, 1440)),"Red rocket combo exists.")
        touch(Template(r"tpl1559339113894.png", record_pos=(0.077, 0.128), resolution=(2960, 1440)))
        sleep(2)
        if exists(Template(r"tpl1559338410199.png", record_pos=(-0.003, -0.151), resolution=(2960, 1440))):
            break;

    if exists(Template(r"tpl1559399271640.png", record_pos=(-0.177, 0.127), resolution=(2960, 1440))):
        assert_exists(Template(r"tpl1559399281857.png", record_pos=(-0.177, 0.13), resolution=(2960, 1440)), "Purple rocket combo exists")
        touch(Template(r"tpl1559399311477.png", record_pos=(-0.176, 0.129), resolution=(2960, 1440)))
        sleep(2)
        if exists(Template(r"tpl1559338410199.png", record_pos=(-0.003, -0.151), resolution=(2960, 1440))):
            break;
    if exists(Template(r"tpl1559481968153.png", record_pos=(0.149, 0.082), resolution=(2960, 1440))):
        assert_exists(Template(r"tpl1559481968153.png", record_pos=(0.149, 0.082), resolution=(2960, 1440)),"Orange rocket combo exists")
        touch(Template(r"tpl1559481968153.png", record_pos=(0.149, 0.082), resolution=(2960, 1440)))
        sleep(2)
        if exists(Template(r"tpl1559338410199.png", record_pos=(-0.003, -0.151), resolution=(2960, 1440))):
            break;
    if exists(Template(r"tpl1559399622974.png", record_pos=(-0.176, 0.081), resolution=(2960, 1440))):
        assert_exists(Template(r"tpl1559399631384.png", record_pos=(-0.176, 0.082), resolution=(2960, 1440)), "Yellow bomb combo exists.")
        touch(Template(r"tpl1559399650447.png", record_pos=(-0.176, 0.082), resolution=(2960, 1440)))
        sleep(2)
        if exists(Template(r"tpl1559338410199.png", record_pos=(-0.003, -0.151), resolution=(2960, 1440))):
            break;

    if exists(Template(r"tpl1559401174340.png", record_pos=(-0.085, 0.082), resolution=(2960, 1440))):
        assert_exists(Template(r"tpl1559401180808.png", record_pos=(-0.084, 0.081), resolution=(2960, 1440)), "Blue bomb exists.")
        touch(Template(r"tpl1559401210775.png", record_pos=(-0.084, 0.082), resolution=(2960, 1440)))
        sleep(2)
        if exists(Template(r"tpl1559338410199.png", record_pos=(-0.003, -0.151), resolution=(2960, 1440))):
            break;

    if exists(Template(r"tpl1559401038550.png", record_pos=(0.101, 0.035), resolution=(2960, 1440))):
        assert_exists(Template(r"tpl1559401054020.png", record_pos=(0.147, 0.082), resolution=(2960, 1440)), "Pink bomb combo exists.")
        touch(Template(r"tpl1559401068047.png", record_pos=(0.145, 0.082), resolution=(2960, 1440)))
        sleep(2)
        if exists(Template(r"tpl1559338410199.png", record_pos=(-0.003, -0.151), resolution=(2960, 1440))):
            break;

    if exists(Template(r"tpl1559401322187.png", record_pos=(0.054, 0.082), resolution=(2960, 1440))):
        assert_exists(Template(r"tpl1559401342445.png", record_pos=(0.01, 0.082), resolution=(2960, 1440)), "Red bomb combo exists.")
        touch(Template(r"tpl1559401362086.png", record_pos=(0.008, 0.082), resolution=(2960, 1440)))
        sleep(2)
        if exists(Template(r"tpl1559338410199.png", record_pos=(-0.003, -0.151), resolution=(2960, 1440))):
            break;

    if exists(Template(r"tpl1559399494173.png", record_pos=(-0.176, 0.129), resolution=(2960, 1440))):
        assert_exists(Template(r"tpl1559399511592.png", record_pos=(-0.177, 0.129), resolution=(2960, 1440)), "Purple bomb combo exists.")
        touch(Template(r"tpl1559399528605.png", record_pos=(-0.176, 0.127), resolution=(2960, 1440)))
        sleep(2)
        if exists(Template(r"tpl1559338410199.png", record_pos=(-0.003, -0.151), resolution=(2960, 1440))):
            break;
    if exists(Template(r"tpl1559482547667.png", record_pos=(-0.223, 0.083), resolution=(2960, 1440))):
        assert_exists(Template(r"tpl1559482547667.png", record_pos=(-0.223, 0.083), resolution=(2960, 1440)),"Orange bomb combo exists")
        touch(Template(r"tpl1559482547667.png", record_pos=(-0.223, 0.083), resolution=(2960, 1440)))
        sleep(2)
        if exists(Template(r"tpl1559338410199.png", record_pos=(-0.003, -0.151), resolution=(2960, 1440))):
            break;
    if exists(Template(r"tpl1559339124359.png", record_pos=(-0.108, 0.084), resolution=(2960, 1440))):
        assert_exists(Template(r"tpl1559339132078.png", record_pos=(-0.108, 0.081), resolution=(2960, 1440)), "Red spiral combo exists.")
        touch(Template(r"tpl1559339132078.png", record_pos=(-0.108, 0.081), resolution=(2960, 1440)))
        sleep(2)
        if exists(Template(r"tpl1559338410199.png", record_pos=(-0.003, -0.151), resolution=(2960, 1440))):
            break;

        if exists(Template(r"tpl1559401422533.png", record_pos=(0.009, 0.087), resolution=(2960, 1440))):
            assert_exists(Template(r"tpl1559401422533.png", record_pos=(0.009, 0.087), resolution=(2960, 1440)), "Red bottle exists.")
            touch(Template(r"tpl1559401422533.png", record_pos=(0.009, 0.087), resolution=(2960, 1440)))
            sleep(2)
            if exists(Template(r"tpl1559338410199.png", record_pos=(-0.003, -0.151), resolution=(2960, 1440))):
                break;

    if exists(Template(r"tpl1559400345129.png", record_pos=(-0.178, 0.128), resolution=(2960, 1440))):
        assert_exists(Template(r"tpl1559400353241.png", record_pos=(-0.178, 0.128), resolution=(2960, 1440)), "Yellow spiral combo exists.")
        touch(Template(r"tpl1559400371182.png", record_pos=(-0.177, 0.13), resolution=(2960, 1440)))
        sleep(2)
        if exists(Template(r"tpl1559338410199.png", record_pos=(-0.003, -0.151), resolution=(2960, 1440))):
            break;

        if exists(Template(r"tpl1559400414569.png", record_pos=(-0.177, 0.176), resolution=(2960, 1440))):
            assert_exists(Template(r"tpl1559400423040.png", record_pos=(-0.177, 0.175), resolution=(2960, 1440)), "Yellow bottle exists.")
            touch(Template(r"tpl1559400436620.png", record_pos=(-0.176, 0.179), resolution=(2960, 1440)))
            sleep(2)
            if exists(Template(r"tpl1559338410199.png", record_pos=(-0.003, -0.151), resolution=(2960, 1440))):
                break;

    if exists(Template(r"tpl1559400498212.png", record_pos=(-0.176, 0.128), resolution=(2960, 1440))):
        assert_exists(Template(r"tpl1559400513223.png", record_pos=(-0.129, 0.175), resolution=(2960, 1440)), "Blue spiral combo exists.")
        touch(Template(r"tpl1559400530442.png", record_pos=(-0.131, 0.174), resolution=(2960, 1440)))
        sleep(2)
        if exists(Template(r"tpl1559338410199.png", record_pos=(-0.003, -0.151), resolution=(2960, 1440))):
            break;

        if exists(Template(r"tpl1559400563423.png", record_pos=(-0.131, 0.178), resolution=(2960, 1440))):
            assert_exists(Template(r"tpl1559400572381.png", record_pos=(-0.132, 0.175), resolution=(2960, 1440)), "Blue bottle exists.")
            touch(Template(r"tpl1559400587283.png", record_pos=(-0.131, 0.175), resolution=(2960, 1440)))
            sleep(2)
            if exists(Template(r"tpl1559338410199.png", record_pos=(-0.003, -0.151), resolution=(2960, 1440))):
                break;

    if exists(Template(r"tpl1559400645070.png", record_pos=(0.146, 0.129), resolution=(2960, 1440))):
        assert_exists(Template(r"tpl1559400661585.png", record_pos=(0.149, 0.129), resolution=(2960, 1440)), "Pink spiral combo exists.")
        touch(Template(r"tpl1559400674972.png", record_pos=(0.151, 0.128), resolution=(2960, 1440)))
        sleep(2)
        if exists(Template(r"tpl1559338410199.png", record_pos=(-0.003, -0.151), resolution=(2960, 1440))):
            break;

        if exists(Template(r"tpl1559400705975.png", record_pos=(0.146, 0.13), resolution=(2960, 1440))):
            assert_exists(Template(r"tpl1559400725473.png", record_pos=(0.147, 0.13), resolution=(2960, 1440)),"Pink bottle exists.")
            touch(Template(r"tpl1559400750990.png", record_pos=(0.146, 0.131), resolution=(2960, 1440)))
            sleep(2)    
            if exists(Template(r"tpl1559338410199.png", record_pos=(-0.003, -0.151), resolution=(2960, 1440))):
                break;

        if exists(Template(r"tpl1559400822202.png", record_pos=(0.008, 0.036), resolution=(2960, 1440))):
            assert_exists(Template(r"tpl1559400831004.png", record_pos=(0.009, 0.036), resolution=(2960, 1440)), "Purple spiral combo exists.")
            touch(Template(r"tpl1559400853864.png", record_pos=(0.01, 0.036), resolution=(2960, 1440)))
            sleep(2)
            if exists(Template(r"tpl1559338410199.png", record_pos=(-0.003, -0.151), resolution=(2960, 1440))):
                break;

            if exists(Template(r"tpl1559400880391.png", record_pos=(0.009, 0.087), resolution=(2960, 1440))):
                assert_exists(Template(r"tpl1559400891298.png", record_pos=(0.008, 0.085), resolution=(2960, 1440)), "Purple bottle exists.")
                touch(Template(r"tpl1559400906104.png", record_pos=(0.008, 0.082), resolution=(2960, 1440)))
                sleep(2)
                if exists(Template(r"tpl1559338410199.png", record_pos=(-0.003, -0.151), resolution=(2960, 1440))):
                    break;
        if exists(Template(r"tpl1559482063006.png", record_pos=(-0.084, 0.176), resolution=(2960, 1440))):
            assert_exists(Template(r"tpl1559482063006.png", record_pos=(-0.084, 0.176), resolution=(2960, 1440)),"Spiral orange combo exists")
            touch(Template(r"tpl1559482063006.png", record_pos=(-0.084, 0.176), resolution=(2960, 1440)))
            sleep(2)
            if exists(Template(r"tpl1559482112705.png", record_pos=(-0.084, 0.178), resolution=(2960, 1440))):
                assert_exists(Template(r"tpl1559482112705.png", record_pos=(-0.084, 0.178), resolution=(2960, 1440)),"Orange bottle exists")
                touch(Template(r"tpl1559482112705.png", record_pos=(-0.084, 0.178), resolution=(2960, 1440)))
                sleep(2)
                if exists(Template(r"tpl1559338410199.png", record_pos=(-0.003, -0.151), resolution=(2960, 1440))):
                    break;


if exists(Template(r"tpl1559338464378.png", record_pos=(0.002, -0.149), resolution=(2960, 1440))):
    touch(Template(r"tpl1559338476449.png", record_pos=(0.104, 0.142), resolution=(2960, 1440)))
    assert_exists(Template(r"tpl1559340077794.png", record_pos=(-0.01, -0.15), resolution=(2960, 1440)), "Level fail scene works.")
    touch(Template(r"tpl1559340104251.png", record_pos=(0.001, 0.127), resolution=(2960, 1440)))
    if exists(Template(r"tpl1559404279780.png", record_pos=(-0.004, -0.129), resolution=(2960, 1440))):
        assert_exists(Template(r"tpl1559404298429.png", record_pos=(-0.001, -0.13), resolution=(2960, 1440)),"No more lives.")
        home()
    else:
        assert_exists(Template(r"tpl1559401498831.png", record_pos=(-0.444, 0.115), resolution=(2960, 1440)), "Replay works.")
        home()
elif exists(Template(r"tpl1559398755616.png", record_pos=(0.005, -0.059), resolution=(2960, 1440))):
    assert_exists(Template(r"tpl1559398766858.png", record_pos=(0.006, -0.052), resolution=(2960, 1440)), "Level passed.")
    touch(Template(r"tpl1559398791593.png", record_pos=(-0.007, 0.005), resolution=(2960, 1440)))
    home()
if exists(Template(r"tpl1559404279780.png", record_pos=(-0.004, -0.129), resolution=(2960, 1440))):
    assert_exists(Template(r"tpl1559404298429.png", record_pos=(-0.001, -0.13), resolution=(2960, 1440)),"No more lives.")
    home()


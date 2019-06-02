# -*- encoding=utf8 -*-
__author__ = "Adrian"

from airtest.core.api import *
import sys

auto_setup(__file__)

start_app("dk.tactile.lilysgarden")


wait(Template(r"1.png", record_pos=(0.18, 0.173), resolution=(2960, 1440)))

touch(Template(r"2.png", record_pos=(-0.004, 0.181), resolution=(2960, 1440)))
if exists(Template(r"3.png", record_pos=(-0.003, -0.143), resolution=(2960, 1440))):
    touch(Template(r"4.png", record_pos=(0.183, -0.142), resolution=(2960, 1440)))

touch(Template(r"5.png", record_pos=(0.385, 0.17), resolution=(2960, 1440)))
touch(Template(r"6.png", record_pos=(0.002, 0.127), resolution=(2960, 1440)))
sleep(2)
assert_exists(Template(r"7.png", record_pos=(-0.444, 0.113), resolution=(2960, 1440)), "Stage start works.")
touch(Template(r"8.png", record_pos=(-0.305, -0.176), resolution=(2960, 1440)))
while not exists(Template(r"9.png", record_pos=(-0.003, -0.151), resolution=(2960, 1440))):
    sleep(2)
    if exists(Template(r"10.png", record_pos=(-0.236, 0.13), resolution=(2960, 1440))):
        assert_exists(Template(r"11.png", record_pos=(-0.236, 0.13), resolution=(2960, 1440)), "Combo of 2+ horizontal blue flowers exist.")

        touch(Template(r"12.png", record_pos=(-0.236, 0.13), resolution=(2960, 1440)))
        sleep(2)
        if exists(Template(r"13.png", record_pos=(-0.003, -0.151), resolution=(2960, 1440))):
            break;
    if exists(Template(r"14.png", record_pos=(0.17, 0.05), resolution=(2960, 1440))):
        assert_exists(Template(r"15.png", record_pos=(0.17, 0.05), resolution=(2960, 1440)),"Combo of 2+ blue flowers exist.")

        touch(Template(r"16.png", record_pos=(0.17, 0.05), resolution=(2960, 1440)))        
        sleep(2)
        if exists(Template(r"17.png", record_pos=(-0.003, -0.151), resolution=(2960, 1440))):
            break;

    if exists(Template(r"18.png", record_pos=(0.121, -0.011), resolution=(2960, 1440))):
        assert_exists(Template(r"19.png", record_pos=(0.121, -0.011), resolution=(2960, 1440)), "Combo of 2+ pink flowers exist.")
        touch(Template(r"20.png", record_pos=(0.121, -0.011), resolution=(2960, 1440)))
        sleep(2)
        if exists(Template(r"21.png", record_pos=(-0.003, -0.151), resolution=(2960, 1440))):
            break;

    if exists(Template(r"22.png", record_pos=(-0.107, 0.142), resolution=(2960, 1440))):
        assert_exists(Template(r"23.png", record_pos=(-0.107, 0.142), resolution=(2960, 1440)), "Combo of 2+ pink flowers exist.")

        touch(Template(r"24.png", record_pos=(-0.107, 0.142), resolution=(2960, 1440)))
        sleep(2)
        if exists(Template(r"25.png", record_pos=(-0.003, -0.151), resolution=(2960, 1440))):
            break;

    if exists(Template(r"26.png", record_pos=(-0.154, 0.141), resolution=(2960, 1440))):
        assert_exists(Template(r"27.png", record_pos=(-0.154, 0.141), resolution=(2960, 1440)), "Combo of 2+ yellow flowers exist.")

        touch(Template(r"28.png", record_pos=(-0.154, 0.141), resolution=(2960, 1440)))
        sleep(2)
        if exists(Template(r"29.png", record_pos=(-0.003, -0.151), resolution=(2960, 1440))):
            break;

    if exists(Template(r"31.png", record_pos=(-0.143, -0.055), resolution=(2960, 1440))):
        assert_exists(Template(r"32.png", record_pos=(-0.143, -0.055), resolution=(2960, 1440)), "Combo of 2+ yellow flowers exist.")
        touch(Template(r"33.png", record_pos=(-0.143, -0.055), resolution=(2960, 1440)))
        sleep(2)
        if exists(Template(r"34.png", record_pos=(-0.003, -0.151), resolution=(2960, 1440))):
            break;

    if exists(Template(r"35.png", record_pos=(-0.107, -0.128), resolution=(2960, 1440))):
        assert_exists(Template(r"36.png", record_pos=(-0.107, -0.125), resolution=(2960, 1440)),"Combo of 2+ red flowers exist.")
        touch(Template(r"37.png", record_pos=(-0.107, -0.125), resolution=(2960, 1440)))
        sleep(2)
        if exists(Template(r"34.png", record_pos=(-0.003, -0.151), resolution=(2960, 1440))):
            break;

    if exists(Template(r"39.png", record_pos=(0.145, 0.175), resolution=(2960, 1440))):
        assert_exists(Template(r"39.png", record_pos=(0.145, 0.175), resolution=(2960, 1440)),"Combo of 2+ red flowers exist.")
        touch(Template(r"40.png", record_pos=(0.145, 0.175), resolution=(2960, 1440)))
        sleep(2)
        if exists(Template(r"41.png", record_pos=(-0.003, -0.151), resolution=(2960, 1440))):
            break;

    if exists(Template(r"42.png", record_pos=(0.177, -0.01), resolution=(2960, 1440))):
        assert_exists(Template(r"43.png", record_pos=(0.177, -0.01), resolution=(2960, 1440)), "Combo of 2+ purple flowers exist.")
        touch(Template(r"44.png", record_pos=(0.177, -0.01), resolution=(2960, 1440)))

        sleep(2)
        if exists(Template(r"45.png", record_pos=(-0.003, -0.151), resolution=(2960, 1440))):
            break;

    if exists(Template(r"46.png", record_pos=(0.216, -0.046), resolution=(2960, 1440))):
        assert_exists(Template(r"47.png", record_pos=(0.216, -0.046), resolution=(2960, 1440)), "Combo of 2+ purple flowers exist.")
        touch(Template(r"48.png", record_pos=(0.216, -0.046), resolution=(2960, 1440)))
        sleep(2)
        if exists(Template(r"49.png", record_pos=(-0.003, -0.151), resolution=(2960, 1440))):
            break;

    if exists(Template(r"50.png", record_pos=(0.017, 0.108), resolution=(2960, 1440))):
        assert_exists(Template(r"51.png", record_pos=(0.017, 0.108), resolution=(2960, 1440)),"Combo of 2+ orange flowers exist.")
        touch(Template(r"52.png", record_pos=(0.017, 0.108), resolution=(2960, 1440)))
        sleep(2) 
        if exists(Template(r"53.png", record_pos=(-0.003, -0.151), resolution=(2960, 1440))):
            break;
    if exists(Template(r"54.png", record_pos=(0.285, 0.097), resolution=(2960, 1440))):
        assert_exists(Template(r"55.png", record_pos=(0.285, 0.097), resolution=(2960, 1440)),"Combo of 2+ orange flowers exist")
        touch(Template(r"56.png", record_pos=(0.285, 0.097), resolution=(2960, 1440)))
        sleep(2)
        if exists(Template(r"57.png", record_pos=(-0.003, -0.151), resolution=(2960, 1440))):
            break;


    if exists(Template(r"58.png", record_pos=(0.215, 0.13), resolution=(2960, 1440))):
        assert_exists(Template(r"59.png", record_pos=(-0.083, 0.179), resolution=(2960, 1440)), "Diagonal rocket exists.")
        touch(Template(r"60.png", record_pos=(0.215, 0.131), resolution=(2960, 1440)))
        sleep(2)
        if exists(Template(r"61.png", record_pos=(-0.003, -0.151), resolution=(2960, 1440))):
            break;

    if exists(Template(r"62.png", record_pos=(-0.155, -0.054), resolution=(2960, 1440))):
        assert_exists(Template(r"63.png", record_pos=(0.147, 0.086), resolution=(2960, 1440)), "Horizontal rocket exists.")
        touch(Template(r"64.png", record_pos=(-0.153, -0.052), resolution=(2960, 1440)))
        sleep(2)
        if exists(Template(r"65.png", record_pos=(-0.003, -0.151), resolution=(2960, 1440))):
            break;

    if exists(Template(r"66.png", record_pos=(0.168, 0.086), resolution=(2960, 1440))):
        assert_exists(Template(r"67.png", record_pos=(-0.176, 0.133), resolution=(2960, 1440)), "Bomb exists.")
        touch(Template(r"68.png", record_pos=(0.169, 0.086), resolution=(2960, 1440)))
        sleep(2)
        if exists(Template(r"69.png", record_pos=(-0.003, -0.151), resolution=(2960, 1440))):
            break;

    if exists(Template(r"70.png", record_pos=(-0.2, 0.038), resolution=(2960, 1440))):
        assert_exists(Template(r"71.png", record_pos=(-0.176, 0.128), resolution=(2960, 1440)), "Blue rocket combo exists.")
        touch(Template(r"72.png", record_pos=(-0.2, 0.036), resolution=(2960, 1440)))
        sleep(2)
        if exists(Template(r"73.png", record_pos=(-0.003, -0.151), resolution=(2960, 1440))):
            break;

    if exists(Template(r"74.png", record_pos=(-0.155, -0.009), resolution=(2960, 1440))):
        assert_exists(Template(r"75.png", record_pos=(-0.131, 0.081), resolution=(2960, 1440)), "Yellow rocket combo exists.")
        touch(Template(r"76.png", record_pos=(-0.154, -0.01), resolution=(2960, 1440)))
        sleep(2)
        if exists(Template(r"77.png", record_pos=(-0.003, -0.151), resolution=(2960, 1440))):
            break;

    if exists(Template(r"78.png", record_pos=(0.078, 0.036), resolution=(2960, 1440))):
        assert_exists(Template(r"79.png", record_pos=(0.147, -0.01), resolution=(2960, 1440)), "Pink rocket combo exists.")
        touch(Template(r"80 .png", record_pos=(0.078, 0.035), resolution=(2960, 1440)))
        sleep(2)
        if exists(Template(r"81.png", record_pos=(-0.003, -0.151), resolution=(2960, 1440))):
            break;

    if exists(Template(r"82.png", record_pos=(0.078, 0.127), resolution=(2960, 1440))):
        assert_exists(Template(r"83.png", record_pos=(0.077, 0.128), resolution=(2960, 1440)),"Red rocket combo exists.")
        touch(Template(r"84.png", record_pos=(0.077, 0.128), resolution=(2960, 1440)))
        sleep(2)
        if exists(Template(r"85.png", record_pos=(-0.003, -0.151), resolution=(2960, 1440))):
            break;

    if exists(Template(r"86.png", record_pos=(-0.177, 0.127), resolution=(2960, 1440))):
        assert_exists(Template(r"87.png", record_pos=(-0.177, 0.13), resolution=(2960, 1440)), "Purple rocket combo exists")
        touch(Template(r"88.png", record_pos=(-0.176, 0.129), resolution=(2960, 1440)))
        sleep(2)
        if exists(Template(r"89.png", record_pos=(-0.003, -0.151), resolution=(2960, 1440))):
            break;
    if exists(Template(r"90.png", record_pos=(0.149, 0.082), resolution=(2960, 1440))):
        assert_exists(Template(r"91.png", record_pos=(0.149, 0.082), resolution=(2960, 1440)),"Orange rocket combo exists")
        touch(Template(r"92.png", record_pos=(0.149, 0.082), resolution=(2960, 1440)))
        sleep(2)
        if exists(Template(r"93.png", record_pos=(-0.003, -0.151), resolution=(2960, 1440))):
            break;
    if exists(Template(r"94.png", record_pos=(-0.176, 0.081), resolution=(2960, 1440))):
        assert_exists(Template(r"95.png", record_pos=(-0.176, 0.082), resolution=(2960, 1440)), "Yellow bomb combo exists.")
        touch(Template(r"96.png", record_pos=(-0.176, 0.082), resolution=(2960, 1440)))
        sleep(2)
        if exists(Template(r"97.png", record_pos=(-0.003, -0.151), resolution=(2960, 1440))):
            break;

    if exists(Template(r"98.png", record_pos=(-0.085, 0.082), resolution=(2960, 1440))):
        assert_exists(Template(r"99.png", record_pos=(-0.084, 0.081), resolution=(2960, 1440)), "Blue bomb exists.")
        touch(Template(r"100.png", record_pos=(-0.084, 0.082), resolution=(2960, 1440)))
        sleep(2)
        if exists(Template(r"101 .png", record_pos=(-0.003, -0.151), resolution=(2960, 1440))):
            break;

    if exists(Template(r"102.png", record_pos=(0.101, 0.035), resolution=(2960, 1440))):
        assert_exists(Template(r"103.png", record_pos=(0.147, 0.082), resolution=(2960, 1440)), "Pink bomb combo exists.")
        touch(Template(r"104.png", record_pos=(0.145, 0.082), resolution=(2960, 1440)))
        sleep(2)
        if exists(Template(r"105.png", record_pos=(-0.003, -0.151), resolution=(2960, 1440))):
            break;

    if exists(Template(r"106.png", record_pos=(0.054, 0.082), resolution=(2960, 1440))):
        assert_exists(Template(r"107.png", record_pos=(0.01, 0.082), resolution=(2960, 1440)), "Red bomb combo exists.")
        touch(Template(r"108.png", record_pos=(0.008, 0.082), resolution=(2960, 1440)))
        sleep(2)
        if exists(Template(r"109.png", record_pos=(-0.003, -0.151), resolution=(2960, 1440))):
            break;

    if exists(Template(r"110.png", record_pos=(-0.176, 0.129), resolution=(2960, 1440))):
        assert_exists(Template(r"111.png", record_pos=(-0.177, 0.129), resolution=(2960, 1440)), "Purple bomb combo exists.")
        touch(Template(r"112.png", record_pos=(-0.176, 0.127), resolution=(2960, 1440)))
        sleep(2)
        if exists(Template(r"113.png", record_pos=(-0.003, -0.151), resolution=(2960, 1440))):
            break;
    if exists(Template(r"114.png", record_pos=(-0.223, 0.083), resolution=(2960, 1440))):
        assert_exists(Template(r"115.png", record_pos=(-0.223, 0.083), resolution=(2960, 1440)),"Orange bomb combo exists")
        touch(Template(r"116.png", record_pos=(-0.223, 0.083), resolution=(2960, 1440)))
        sleep(2)
        if exists(Template(r"117.png", record_pos=(-0.003, -0.151), resolution=(2960, 1440))):
            break;
    if exists(Template(r"118.png", record_pos=(-0.108, 0.084), resolution=(2960, 1440))):
        assert_exists(Template(r"119.png", record_pos=(-0.108, 0.081), resolution=(2960, 1440)), "Red spiral combo exists.")
        touch(Template(r"120.png", record_pos=(-0.108, 0.081), resolution=(2960, 1440)))
        sleep(2)
        if exists(Template(r"121.png", record_pos=(-0.003, -0.151), resolution=(2960, 1440))):
            break;

        if exists(Template(r"122.png", record_pos=(0.009, 0.087), resolution=(2960, 1440))):
            assert_exists(Template(r"123.png", record_pos=(0.009, 0.087), resolution=(2960, 1440)), "Red bottle exists.")
            touch(Template(r"124.png", record_pos=(0.009, 0.087), resolution=(2960, 1440)))
            sleep(2)
            if exists(Template(r"125.png", record_pos=(-0.003, -0.151), resolution=(2960, 1440))):
                break;

    if exists(Template(r"126.png", record_pos=(-0.178, 0.128), resolution=(2960, 1440))):
        assert_exists(Template(r"127.png", record_pos=(-0.178, 0.128), resolution=(2960, 1440)), "Yellow spiral combo exists.")
        touch(Template(r"127.png", record_pos=(-0.177, 0.13), resolution=(2960, 1440)))
        sleep(2)
        if exists(Template(r"128.png", record_pos=(-0.003, -0.151), resolution=(2960, 1440))):
            break;

        if exists(Template(r"129.png", record_pos=(-0.177, 0.176), resolution=(2960, 1440))):
            assert_exists(Template(r"130 .png", record_pos=(-0.177, 0.175), resolution=(2960, 1440)), "Yellow bottle exists.")
            touch(Template(r"131.png", record_pos=(-0.176, 0.179), resolution=(2960, 1440)))
            sleep(2)
            if exists(Template(r"132.png", record_pos=(-0.003, -0.151), resolution=(2960, 1440))):
                break;

    if exists(Template(r"133.png", record_pos=(-0.176, 0.128), resolution=(2960, 1440))):
        assert_exists(Template(r"134.png", record_pos=(-0.129, 0.175), resolution=(2960, 1440)), "Blue spiral combo exists.")
        touch(Template(r"135.png", record_pos=(-0.131, 0.174), resolution=(2960, 1440)))
        sleep(2)
        if exists(Template(r"136.png", record_pos=(-0.003, -0.151), resolution=(2960, 1440))):
            break;

        if exists(Template(r"137.png", record_pos=(-0.131, 0.178), resolution=(2960, 1440))):
            assert_exists(Template(r"138.png", record_pos=(-0.132, 0.175), resolution=(2960, 1440)), "Blue bottle exists.")
            touch(Template(r"139.png", record_pos=(-0.131, 0.175), resolution=(2960, 1440)))
            sleep(2)
            if exists(Template(r"140.png", record_pos=(-0.003, -0.151), resolution=(2960, 1440))):
                break;

    if exists(Template(r"141.png", record_pos=(0.146, 0.129), resolution=(2960, 1440))):
        assert_exists(Template(r"142.png", record_pos=(0.149, 0.129), resolution=(2960, 1440)), "Pink spiral combo exists.")
        touch(Template(r"143.png", record_pos=(0.151, 0.128), resolution=(2960, 1440)))
        sleep(2)
        if exists(Template(r"144.png", record_pos=(-0.003, -0.151), resolution=(2960, 1440))):
            break;

        if exists(Template(r"145.png", record_pos=(0.146, 0.13), resolution=(2960, 1440))):
            assert_exists(Template(r"146.png", record_pos=(0.147, 0.13), resolution=(2960, 1440)),"Pink bottle exists.")
            touch(Template(r"147.png", record_pos=(0.146, 0.131), resolution=(2960, 1440)))
            sleep(2)    
            if exists(Template(r"148.png", record_pos=(-0.003, -0.151), resolution=(2960, 1440))):
                break;

        if exists(Template(r"149.png", record_pos=(0.008, 0.036), resolution=(2960, 1440))):
            assert_exists(Template(r"150.png", record_pos=(0.009, 0.036), resolution=(2960, 1440)), "Purple spiral combo exists.")
            touch(Template(r"151.png", record_pos=(0.01, 0.036), resolution=(2960, 1440)))
            sleep(2)
            if exists(Template(r"152.png", record_pos=(-0.003, -0.151), resolution=(2960, 1440))):
                break;

            if exists(Template(r"153.png", record_pos=(0.009, 0.087), resolution=(2960, 1440))):
                assert_exists(Template(r"154.png", record_pos=(0.008, 0.085), resolution=(2960, 1440)), "Purple bottle exists.")
                touch(Template(r"155.png", record_pos=(0.008, 0.082), resolution=(2960, 1440)))
                sleep(2)
                if exists(Template(r"156.png", record_pos=(-0.003, -0.151), resolution=(2960, 1440))):
                    break;
        if exists(Template(r"157.png", record_pos=(-0.084, 0.176), resolution=(2960, 1440))):
            assert_exists(Template(r"158.png", record_pos=(-0.084, 0.176), resolution=(2960, 1440)),"Spiral orange combo exists")
            touch(Template(r"tpl1559482063006.png", record_pos=(-0.084, 0.176), resolution=(2960, 1440)))
            sleep(2)
            if exists(Template(r"159.png", record_pos=(-0.084, 0.178), resolution=(2960, 1440))):
                assert_exists(Template(r"160.png", record_pos=(-0.084, 0.178), resolution=(2960, 1440)),"Orange bottle exists")
                touch(Template(r"161.png", record_pos=(-0.084, 0.178), resolution=(2960, 1440)))
                sleep(2)
                if exists(Template(r"162.png", record_pos=(-0.003, -0.151), resolution=(2960, 1440))):
                    break;


if exists(Template(r"163.png", record_pos=(0.002, -0.149), resolution=(2960, 1440))):
    touch(Template(r"164.png", record_pos=(0.104, 0.142), resolution=(2960, 1440)))
    assert_exists(Template(r"165.png", record_pos=(-0.01, -0.15), resolution=(2960, 1440)), "Level fail scene works.")
    touch(Template(r"166.png", record_pos=(0.001, 0.127), resolution=(2960, 1440)))
    if exists(Template(r"167.png", record_pos=(-0.004, -0.129), resolution=(2960, 1440))):
        assert_exists(Template(r"168.png", record_pos=(-0.001, -0.13), resolution=(2960, 1440)),"No more lives.")
        home()
    else:
        assert_exists(Template(r"169.png", record_pos=(-0.444, 0.115), resolution=(2960, 1440)), "Replay works.")
        home()
elif exists(Template(r"170.png", record_pos=(0.005, -0.059), resolution=(2960, 1440))):
    assert_exists(Template(r"171.png", record_pos=(0.006, -0.052), resolution=(2960, 1440)), "Level passed.")
    touch(Template(r"172.png", record_pos=(-0.007, 0.005), resolution=(2960, 1440)))
    home()
if exists(Template(r"174.png", record_pos=(-0.004, -0.129), resolution=(2960, 1440))):
    assert_exists(Template(r"177.png", record_pos=(-0.001, -0.13), resolution=(2960, 1440)),"No more lives.")
    home()


-- Vcc module test-bench
-- VHDL-2008

library vunit_lib;
context vunit_lib.vunit_context;

entity vcc_tb is
    generic (RUNNER_CFG: string);
end entity;

architecture vcc_tb_arch of vcc_tb is begin
    main: process is begin
        test_runner_setup(runner, RUNNER_CFG);
        report "Hello world!";
        test_runner_cleanup(runner);
    end process;
end architecture;

-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: 02-Jun-2021 às 20:55
-- Versão do servidor: 10.1.38-MariaDB
-- versão do PHP: 7.3.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `tccativos`
--

DELIMITER $$
--
-- Procedures
--
CREATE DEFINER=`root`@`localhost` PROCEDURE `AtualizarQtdEquipSetor` (IN `QTDEQUIP` INT(11), IN `NUMSETOR` INT(11))  BEGIN
UPDATE setores
 SET QtdEquipamentos = QTDEQUIP
 WHERE codSetor = NUMSETOR;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `InserirDefeito` (IN `DEFEITO` INT(11), IN `DESCRICAO` VARCHAR(240), IN `CODEQUIP` INT(11))  BEGIN
INSERT INTO relatoriosdef VALUES
(DEFEITO, DESCRICAO, CODEQUIP);
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `InserirFuncEquip` (IN `FE` INT(11), IN `CODFUNC` INT(11), IN `CODEQUIP` INT)  BEGIN
INSERT INTO funcequip VALUES
(FE, CODFUNC, CODEQUIP);
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `InserirFuncionario` (IN `COD` INT(11), IN `CPF` VARCHAR(14), IN `NOME` VARCHAR(60), IN `CARGO` VARCHAR(60), IN `FUNCAO` VARCHAR(60), IN `SENHA` VARCHAR(60), IN `SETOR` INT(11))  BEGIN
INSERT INTO funcionarios VALUES
(COD,CPF,NOME,CARGO,FUNCAO,md5(SENHA),SETOR);
 END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `InserirFuncSoft` (IN `FS` INT(11), IN `CODFUNC` INT(11), IN `CODSOFT` INT(11))  BEGIN
INSERT INTO funcprecisasofts VALUES
(FS, CODFUNC, CODSOFT);
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `InserirManutencao` (IN `MANUTENCAO` INT(11), IN `CODFUNC` INT(11), IN `CODEQUIP` INT(11), IN `CODDEF` INT)  BEGIN
INSERT INTO manutencao VALUES
(MANUTENCAO, CODFUNC, CODEQUIP, CODDEF);
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `InserirSoftware` (IN `SOFT` INT(11), IN `LISENSA` INT(60), IN `NOME` VARCHAR(240))  BEGIN
INSERT INTO softwares VALUES
(SOFT, LISENSA, NOME);
END$$

DELIMITER ;

-- --------------------------------------------------------

--
-- Estrutura da tabela `equipamentos`
--

CREATE TABLE `equipamentos` (
  `codEquip` int(11) NOT NULL,
  `nomeEquip` varchar(240) NOT NULL,
  `tipoEquip` varchar(240) NOT NULL,
  `dataCompra` date NOT NULL,
  `statusEquip` varchar(50) NOT NULL,
  `quantidadeEquip` int(11) NOT NULL,
  `valorPago` double(10,2) NOT NULL,
  `codSetor` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Acionadores `equipamentos`
--
DELIMITER $$
CREATE TRIGGER `AtualizarEquipamentoAtualizar` AFTER UPDATE ON `equipamentos` FOR EACH ROW BEGIN
SET @somar = NEW.quantidadeEquip;
SELECT sum(quantidadeEquip) into @somar from equipamentos WHERE codSetor = NEW.codSetor;
CALL AtualizarQtdEquipSetor (@somar, NEW.codSetor);
END
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `AtualizarEquipamentoInsert` AFTER INSERT ON `equipamentos` FOR EACH ROW BEGIN
SET @somar = NEW.quantidadeEquip;
SELECT sum(quantidadeEquip) into @somar from equipamentos WHERE codSetor = NEW.codSetor;
CALL AtualizarQtdEquipSetor (@somar, NEW.codSetor);
END
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `AtualizarEquipamentosDeletar` AFTER DELETE ON `equipamentos` FOR EACH ROW BEGIN
SET @somar = OLD.quantidadeEquip;
SELECT sum(quantidadeEquip) into @somar from equipamentos WHERE codSetor = OLD.codSetor;
CALL AtualizarQtdEquipSetor (@somar, OLD.codSetor);
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Stand-in structure for view `equipfunc`
-- (See below for the actual view)
--
CREATE TABLE `equipfunc` (
`codFuncEquip` int(11)
,`nomeFunc` varchar(100)
,`cargo` varchar(100)
,`nomeEquip` varchar(240)
,`tipoEquip` varchar(240)
,`codSetor` int(11)
);

-- --------------------------------------------------------

--
-- Estrutura da tabela `funcequip`
--

CREATE TABLE `funcequip` (
  `codFuncEquip` int(11) NOT NULL,
  `codFunc` int(11) NOT NULL,
  `codEquip` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estrutura da tabela `funcionarios`
--

CREATE TABLE `funcionarios` (
  `codFunc` int(11) NOT NULL,
  `cpf` varchar(14) NOT NULL,
  `nomeFunc` varchar(100) NOT NULL,
  `cargo` varchar(100) NOT NULL,
  `funcao` varchar(60) NOT NULL,
  `senha` varchar(60) NOT NULL,
  `codSetor` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estrutura da tabela `funcprecisasofts`
--

CREATE TABLE `funcprecisasofts` (
  `codFps` int(11) NOT NULL,
  `codFunc` int(11) NOT NULL,
  `codSoft` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Stand-in structure for view `funcsofts`
-- (See below for the actual view)
--
CREATE TABLE `funcsofts` (
`codFps` int(11)
,`nomeFunc` varchar(100)
,`cargo` varchar(100)
,`nomeSoft` varchar(240)
,`NomeLisensa` varchar(60)
,`validade` date
,`codSetor` int(11)
);

-- --------------------------------------------------------

--
-- Stand-in structure for view `infomanutencao`
-- (See below for the actual view)
--
CREATE TABLE `infomanutencao` (
`codManutencao` int(11)
,`nomeFunc` varchar(100)
,`cargo` varchar(100)
,`nomeEquip` varchar(240)
,`tipoEquip` varchar(240)
,`statusEquip` varchar(50)
,`descricao` varchar(240)
,`codSetor` int(11)
);

-- --------------------------------------------------------

--
-- Estrutura da tabela `lisensa`
--

CREATE TABLE `lisensa` (
  `codLisensa` varchar(100) NOT NULL,
  `NomeLisensa` varchar(60) NOT NULL,
  `dataCompra` date NOT NULL,
  `validade` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estrutura da tabela `manutencao`
--

CREATE TABLE `manutencao` (
  `codManutencao` int(11) NOT NULL,
  `codFunc` int(11) NOT NULL,
  `codEquip` int(11) NOT NULL,
  `codDefeito` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estrutura da tabela `relatoriosdef`
--

CREATE TABLE `relatoriosdef` (
  `codDefeito` int(11) NOT NULL,
  `descricao` varchar(240) NOT NULL,
  `codEquip` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estrutura da tabela `setores`
--

CREATE TABLE `setores` (
  `codSetor` int(11) NOT NULL,
  `nomeSetor` varchar(240) NOT NULL,
  `QtdEquipamentos` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estrutura da tabela `softwares`
--

CREATE TABLE `softwares` (
  `codSoft` int(11) NOT NULL,
  `codLisensa` varchar(100) NOT NULL,
  `nomeSoft` varchar(240) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure for view `equipfunc`
--
DROP TABLE IF EXISTS `equipfunc`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `equipfunc`  AS  select `fe`.`codFuncEquip` AS `codFuncEquip`,`f`.`nomeFunc` AS `nomeFunc`,`f`.`cargo` AS `cargo`,`e`.`nomeEquip` AS `nomeEquip`,`e`.`tipoEquip` AS `tipoEquip`,`e`.`codSetor` AS `codSetor` from ((`funcequip` `fe` join `funcionarios` `f`) join `equipamentos` `e`) where ((`fe`.`codFunc` = `f`.`codFunc`) and (`fe`.`codEquip` = `e`.`codEquip`) and (`f`.`codSetor` = `e`.`codSetor`)) order by `f`.`nomeFunc` ;

-- --------------------------------------------------------

--
-- Structure for view `funcsofts`
--
DROP TABLE IF EXISTS `funcsofts`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `funcsofts`  AS  select `fs`.`codFps` AS `codFps`,`f`.`nomeFunc` AS `nomeFunc`,`f`.`cargo` AS `cargo`,`s`.`nomeSoft` AS `nomeSoft`,`l`.`NomeLisensa` AS `NomeLisensa`,`l`.`validade` AS `validade`,`f`.`codSetor` AS `codSetor` from (((`funcprecisasofts` `fs` join `funcionarios` `f`) join `softwares` `s`) join `lisensa` `l`) where ((`fs`.`codFunc` = `f`.`codFunc`) and (`fs`.`codSoft` = `s`.`codSoft`) and (`s`.`codLisensa` = `l`.`codLisensa`)) order by `f`.`nomeFunc` ;

-- --------------------------------------------------------

--
-- Structure for view `infomanutencao`
--
DROP TABLE IF EXISTS `infomanutencao`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `infomanutencao`  AS  select `m`.`codManutencao` AS `codManutencao`,`f`.`nomeFunc` AS `nomeFunc`,`f`.`cargo` AS `cargo`,`e`.`nomeEquip` AS `nomeEquip`,`e`.`tipoEquip` AS `tipoEquip`,`e`.`statusEquip` AS `statusEquip`,`d`.`descricao` AS `descricao`,`e`.`codSetor` AS `codSetor` from (((`manutencao` `m` join `funcionarios` `f`) join `equipamentos` `e`) join `relatoriosdef` `d`) where ((`m`.`codFunc` = `f`.`codFunc`) and (`m`.`codEquip` = `e`.`codEquip`) and (`m`.`codDefeito` = `d`.`codDefeito`) and (`f`.`codSetor` = `e`.`codSetor`) and (`d`.`codEquip` = `e`.`codEquip`)) ;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `equipamentos`
--
ALTER TABLE `equipamentos`
  ADD PRIMARY KEY (`codEquip`),
  ADD KEY `ValorEquipamento` (`valorPago`),
  ADD KEY `codSetor` (`codSetor`);

--
-- Indexes for table `funcequip`
--
ALTER TABLE `funcequip`
  ADD PRIMARY KEY (`codFuncEquip`),
  ADD KEY `funcequip_ibfk_1` (`codFunc`),
  ADD KEY `funcequip_ibfk_2` (`codEquip`);

--
-- Indexes for table `funcionarios`
--
ALTER TABLE `funcionarios`
  ADD PRIMARY KEY (`codFunc`),
  ADD UNIQUE KEY `cpf` (`cpf`),
  ADD KEY `funcao` (`funcao`),
  ADD KEY `funcionarios_ibfk_1` (`codSetor`);

--
-- Indexes for table `funcprecisasofts`
--
ALTER TABLE `funcprecisasofts`
  ADD PRIMARY KEY (`codFps`),
  ADD KEY `funcprecisasofts_ibfk_1` (`codFunc`),
  ADD KEY `funcprecisasofts_ibfk_2` (`codSoft`);

--
-- Indexes for table `lisensa`
--
ALTER TABLE `lisensa`
  ADD PRIMARY KEY (`codLisensa`);

--
-- Indexes for table `manutencao`
--
ALTER TABLE `manutencao`
  ADD PRIMARY KEY (`codManutencao`),
  ADD KEY `manutencao_ibfk_1` (`codFunc`),
  ADD KEY `manutencao_ibfk_2` (`codDefeito`),
  ADD KEY `manutencao_ibfk_3` (`codEquip`);

--
-- Indexes for table `relatoriosdef`
--
ALTER TABLE `relatoriosdef`
  ADD PRIMARY KEY (`codDefeito`),
  ADD KEY `codEquip` (`codEquip`);

--
-- Indexes for table `setores`
--
ALTER TABLE `setores`
  ADD PRIMARY KEY (`codSetor`),
  ADD UNIQUE KEY `EquipPerSetor` (`codSetor`);

--
-- Indexes for table `softwares`
--
ALTER TABLE `softwares`
  ADD PRIMARY KEY (`codSoft`),
  ADD KEY `softwares_ibfk_1` (`codLisensa`);

--
-- Constraints for dumped tables
--

--
-- Limitadores para a tabela `equipamentos`
--
ALTER TABLE `equipamentos`
  ADD CONSTRAINT `codSetor` FOREIGN KEY (`codSetor`) REFERENCES `setores` (`codSetor`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Limitadores para a tabela `funcequip`
--
ALTER TABLE `funcequip`
  ADD CONSTRAINT `funcequip_ibfk_1` FOREIGN KEY (`codFunc`) REFERENCES `funcionarios` (`codFunc`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `funcequip_ibfk_2` FOREIGN KEY (`codEquip`) REFERENCES `equipamentos` (`codEquip`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Limitadores para a tabela `funcionarios`
--
ALTER TABLE `funcionarios`
  ADD CONSTRAINT `funcionarios_ibfk_1` FOREIGN KEY (`codSetor`) REFERENCES `setores` (`codSetor`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Limitadores para a tabela `funcprecisasofts`
--
ALTER TABLE `funcprecisasofts`
  ADD CONSTRAINT `funcprecisasofts_ibfk_1` FOREIGN KEY (`codFunc`) REFERENCES `funcionarios` (`codFunc`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `funcprecisasofts_ibfk_2` FOREIGN KEY (`codSoft`) REFERENCES `softwares` (`codSoft`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Limitadores para a tabela `manutencao`
--
ALTER TABLE `manutencao`
  ADD CONSTRAINT `manutencao_ibfk_1` FOREIGN KEY (`codFunc`) REFERENCES `funcionarios` (`codFunc`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `manutencao_ibfk_2` FOREIGN KEY (`codDefeito`) REFERENCES `relatoriosdef` (`codDefeito`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `manutencao_ibfk_3` FOREIGN KEY (`codEquip`) REFERENCES `equipamentos` (`codEquip`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Limitadores para a tabela `relatoriosdef`
--
ALTER TABLE `relatoriosdef`
  ADD CONSTRAINT `codEquip` FOREIGN KEY (`codEquip`) REFERENCES `equipamentos` (`codEquip`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Limitadores para a tabela `softwares`
--
ALTER TABLE `softwares`
  ADD CONSTRAINT `softwares_ibfk_1` FOREIGN KEY (`codLisensa`) REFERENCES `lisensa` (`codLisensa`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

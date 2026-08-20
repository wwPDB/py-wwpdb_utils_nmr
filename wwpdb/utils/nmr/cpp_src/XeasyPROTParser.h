
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/XeasyPROTParser.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"




class  XeasyPROTParser : public antlr4::Parser {
public:
  enum {
    Integer = 1, Float = 2, SHARP_COMMENT = 3, EXCLM_COMMENT = 4, SMCLN_COMMENT = 5, 
    Simple_name = 6, SPACE = 7, RETURN = 8, ENCLOSE_COMMENT = 9, SECTION_COMMENT = 10, 
    LINE_COMMENT = 11
  };

  enum {
    RuleXeasy_prot = 0, RuleProt = 1, RuleResidue = 2
  };

  explicit XeasyPROTParser(antlr4::TokenStream *input);

  XeasyPROTParser(antlr4::TokenStream *input, const antlr4::atn::ParserATNSimulatorOptions &options);

  ~XeasyPROTParser() override;

  std::string getGrammarFileName() const override;

  const antlr4::atn::ATN& getATN() const override;

  const std::vector<std::string>& getRuleNames() const override;

  const antlr4::dfa::Vocabulary& getVocabulary() const override;

  antlr4::atn::SerializedATNView getSerializedATN() const override;


  class Xeasy_protContext;
  class ProtContext;
  class ResidueContext; 

  class  Xeasy_protContext : public antlr4::ParserRuleContext {
  public:
    Xeasy_protContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> RETURN();
    antlr4::tree::TerminalNode* RETURN(size_t i);
    std::vector<ProtContext *> prot();
    ProtContext* prot(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Xeasy_protContext* xeasy_prot();

  class  ProtContext : public antlr4::ParserRuleContext {
  public:
    ProtContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Integer();
    std::vector<antlr4::tree::TerminalNode *> Float();
    antlr4::tree::TerminalNode* Float(size_t i);
    antlr4::tree::TerminalNode *Simple_name();
    ResidueContext *residue();
    antlr4::tree::TerminalNode *RETURN();
    antlr4::tree::TerminalNode *EOF();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  ProtContext* prot();

  class  ResidueContext : public antlr4::ParserRuleContext {
  public:
    ResidueContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Integer();
    antlr4::tree::TerminalNode *Simple_name();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  ResidueContext* residue();


  // By default the static state used to implement the parser is lazily initialized during the first
  // call to the constructor. You can call this function if you wish to initialize the static state
  // ahead of time.
  static void initialize();

private:
};



// Generated from /home/webmaster/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/CharmmCRDParser.g4 by ANTLR 4.13.0

#pragma once


#include "antlr4-runtime.h"




class  CharmmCRDParser : public antlr4::Parser {
public:
  enum {
    Integer = 1, Float = 2, Double_quote_string = 3, COMMENT = 4, Ext = 5, 
    Simple_name = 6, SPACE = 7, CONTINUE = 8, ENCLOSE_COMMENT = 9, SECTION_COMMENT = 10, 
    LINE_COMMENT = 11, Any_name = 12, SPACE_CM = 13, RETURN_CM = 14
  };

  enum {
    RuleCharmm_crd = 0, RuleComment = 1, RuleCoordinates = 2, RuleAtom_coordinate = 3
  };

  explicit CharmmCRDParser(antlr4::TokenStream *input);

  CharmmCRDParser(antlr4::TokenStream *input, const antlr4::atn::ParserATNSimulatorOptions &options);

  ~CharmmCRDParser() override;

  std::string getGrammarFileName() const override;

  const antlr4::atn::ATN& getATN() const override;

  const std::vector<std::string>& getRuleNames() const override;

  const antlr4::dfa::Vocabulary& getVocabulary() const override;

  antlr4::atn::SerializedATNView getSerializedATN() const override;


  class Charmm_crdContext;
  class CommentContext;
  class CoordinatesContext;
  class Atom_coordinateContext; 

  class  Charmm_crdContext : public antlr4::ParserRuleContext {
  public:
    Charmm_crdContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *EOF();
    std::vector<CommentContext *> comment();
    CommentContext* comment(size_t i);
    std::vector<CoordinatesContext *> coordinates();
    CoordinatesContext* coordinates(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Charmm_crdContext* charmm_crd();

  class  CommentContext : public antlr4::ParserRuleContext {
  public:
    CommentContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *COMMENT();
    antlr4::tree::TerminalNode *RETURN_CM();
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> Any_name();
    antlr4::tree::TerminalNode* Any_name(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  CommentContext* comment();

  class  CoordinatesContext : public antlr4::ParserRuleContext {
  public:
    CoordinatesContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Integer();
    antlr4::tree::TerminalNode *Ext();
    std::vector<Atom_coordinateContext *> atom_coordinate();
    Atom_coordinateContext* atom_coordinate(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  CoordinatesContext* coordinates();

  class  Atom_coordinateContext : public antlr4::ParserRuleContext {
  public:
    Atom_coordinateContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Simple_name();
    antlr4::tree::TerminalNode* Simple_name(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Float();
    antlr4::tree::TerminalNode* Float(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Atom_coordinateContext* atom_coordinate();


  // By default the static state used to implement the parser is lazily initialized during the first
  // call to the constructor. You can call this function if you wish to initialize the static state
  // ahead of time.
  static void initialize();

private:
};



// Generated from /home/webmaster/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/XwinNmrPKParser.g4 by ANTLR 4.13.0

#pragma once


#include "antlr4-runtime.h"




class  XwinNmrPKParser : public antlr4::Parser {
public:
  enum {
    Num_of_dim = 1, Integer = 2, Float = 3, COMMENT = 4, SPACE = 5, RETURN = 6, 
    SECTION_COMMENT = 7, LINE_COMMENT = 8, Annotation = 9, Integer_ND = 10, 
    SPACE_ND = 11, RETURN_ND = 12, Any_name = 13, SPACE_CM = 14, RETURN_CM = 15
  };

  enum {
    RuleXwinnmr_pk = 0, RuleComment = 1, RuleDimension = 2, RulePeak_2d = 3, 
    RulePeak_3d = 4, RulePeak_4d = 5
  };

  explicit XwinNmrPKParser(antlr4::TokenStream *input);

  XwinNmrPKParser(antlr4::TokenStream *input, const antlr4::atn::ParserATNSimulatorOptions &options);

  ~XwinNmrPKParser() override;

  std::string getGrammarFileName() const override;

  const antlr4::atn::ATN& getATN() const override;

  const std::vector<std::string>& getRuleNames() const override;

  const antlr4::dfa::Vocabulary& getVocabulary() const override;

  antlr4::atn::SerializedATNView getSerializedATN() const override;


  class Xwinnmr_pkContext;
  class CommentContext;
  class DimensionContext;
  class Peak_2dContext;
  class Peak_3dContext;
  class Peak_4dContext; 

  class  Xwinnmr_pkContext : public antlr4::ParserRuleContext {
  public:
    Xwinnmr_pkContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> RETURN();
    antlr4::tree::TerminalNode* RETURN(size_t i);
    std::vector<CommentContext *> comment();
    CommentContext* comment(size_t i);
    std::vector<DimensionContext *> dimension();
    DimensionContext* dimension(size_t i);
    std::vector<Peak_2dContext *> peak_2d();
    Peak_2dContext* peak_2d(size_t i);
    std::vector<Peak_3dContext *> peak_3d();
    Peak_3dContext* peak_3d(size_t i);
    std::vector<Peak_4dContext *> peak_4d();
    Peak_4dContext* peak_4d(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Xwinnmr_pkContext* xwinnmr_pk();

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

  class  DimensionContext : public antlr4::ParserRuleContext {
  public:
    DimensionContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Num_of_dim();
    antlr4::tree::TerminalNode *Integer_ND();
    antlr4::tree::TerminalNode *RETURN_ND();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  DimensionContext* dimension();

  class  Peak_2dContext : public antlr4::ParserRuleContext {
  public:
    Peak_2dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Integer();
    std::vector<antlr4::tree::TerminalNode *> Float();
    antlr4::tree::TerminalNode* Float(size_t i);
    antlr4::tree::TerminalNode *RETURN();
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> Annotation();
    antlr4::tree::TerminalNode* Annotation(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Peak_2dContext* peak_2d();

  class  Peak_3dContext : public antlr4::ParserRuleContext {
  public:
    Peak_3dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Integer();
    std::vector<antlr4::tree::TerminalNode *> Float();
    antlr4::tree::TerminalNode* Float(size_t i);
    antlr4::tree::TerminalNode *RETURN();
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> Annotation();
    antlr4::tree::TerminalNode* Annotation(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Peak_3dContext* peak_3d();

  class  Peak_4dContext : public antlr4::ParserRuleContext {
  public:
    Peak_4dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Integer();
    std::vector<antlr4::tree::TerminalNode *> Float();
    antlr4::tree::TerminalNode* Float(size_t i);
    antlr4::tree::TerminalNode *RETURN();
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> Annotation();
    antlr4::tree::TerminalNode* Annotation(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Peak_4dContext* peak_4d();


  // By default the static state used to implement the parser is lazily initialized during the first
  // call to the constructor. You can call this function if you wish to initialize the static state
  // ahead of time.
  static void initialize();

private:
};

